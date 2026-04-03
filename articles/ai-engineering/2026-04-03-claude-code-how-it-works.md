# Claude Code Internals — How It Actually Works

> **Source:** [How Claude Code works (Mintlify)](https://www.mintlify.com/VineeTagarwaL-code/claude-code/concepts/how-it-works)
> **Date:** 2026-04-03
> **Tags:** `#ClaudeCode` `#Architecture` `#AgenticLoop` `#Context` `#ToolExecution`

---

## Overview

Claude Code is a terminal-based coding agent built on a **continuous agentic loop**: read request → reason → call tools → observe results → repeat. It runs entirely in your local terminal process — no remote execution server. Files, shell, and credentials never leave your machine unless an explicit network tool is invoked (e.g., `WebFetch`, `WebSearch`, or an MCP server).

This article breaks down the seven core mechanisms that make it work, based on the leaked source code analysis.

---

## 1. The Agentic Loop — 6-Step Core Cycle

Every interaction follows the same fundamental cycle:

### Step 1: User Sends a Message

The user types in the terminal (Interactive mode) or passes a message via `--print`/stdin (Non-interactive/headless mode). The message is appended to the conversation history.

### Step 2: Context Assembly

Before calling the model, Claude Code assembles a system prompt containing:

- Current date
- Git status (branch, recent commits, working tree state)
- CLAUDE.md memory files
- List of available tools

This context is built by `context.ts` and **memoized for the entire conversation** — it's not recalculated every turn.

### Step 3: Claude Reasons + Selects Tools

The assembled conversation is sent to the Anthropic API. The model reasons about the task and emits one or more `tool_use` blocks, each containing a **tool name + structured JSON input**.

### Step 4: Permission Check

Before executing each tool call, Claude Code evaluates the current permission mode and allow/deny rules. Three possible outcomes:

- **allow** — Tool runs immediately
- **ask** — User confirmation dialog is shown
- **deny** — Tool call is rejected; model receives an error result

### Step 5: Tool Executes + Returns Result

Approved tools run. Results (file contents, command output, search hits) are appended to the conversation as `tool_result` blocks.

### Step 6: Loop Continues

The model receives tool results and either calls more tools or produces a final text response. **The loop repeats until no tool calls remain in a model turn.**

---

## 2. Context Loading — What Gets Injected at Session Start

Two context blocks are prepended to every API call:

### System Context (`getSystemContext()`)

- **Git status** — Current branch, default/main branch, git username, `git status --short` output (truncated at 2,000 chars), last 5 commits from `git log --oneline`
- **Cache-breaking injection** — An ephemeral string used internally to bust the server-side prompt cache during debugging
- Skipped when `CLAUDE_CODE_REMOTE=1` is set (remote/cloud mode)

### User Context (`getUserContext()`)

- **CLAUDE.md memory** — All memory files discovered by the 4-level hierarchy: managed → user → project → local. Can be disabled with `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1`
- **Current date** — Injected as `Today's date is YYYY-MM-DD` so the model always knows the date

### Memoization Strategy

Both context blocks are cached via `lodash/memoize` **for the entire conversation**. Calculated once on the first API call, then reused for subsequent turns. Calling `setSystemPromptInjection()` clears the cache immediately.

---

## 3. Tool Execution Model — The Permission System

Claude Code does **not** execute tool calls autonomously by default. Every tool has a `checkPermissions` method returning one of three results:

| Result | Behavior |
|--------|----------|
| `allow` | Runs immediately, result appended to conversation |
| `ask` | Pauses and shows a confirmation dialog |
| `deny` | Rejected; model receives an error result |

### Permission Modes

- **`bypassPermissions`** — All checks skipped. Fully autonomous execution (for CI/CD, scripting)
- **`acceptEdits`** — File edit tools (`Edit`, `Write`) are auto-approved, but bash commands still require confirmation
- **Default mode** — All write operations require user confirmation

**Exception:** Read-only tools (`Read`, `Glob`, `Grep`) are **auto-approved across all modes** — they're considered safe since they only read.

---

## 4. Interactive vs Non-Interactive Mode

### Interactive (REPL) Mode

The default experience. Renders a live terminal UI using **React/Ink**:

- Streaming token output (tokens displayed as they're generated)
- Tool-use confirmation dialogs
- Spinner animations
- Messages persist within the session

### Non-Interactive (Print) Mode

Activated with `--print` flag or by piping stdin:

- No UI rendered
- Output written to stdout
- Designed for CI/CD pipelines and script automation
- One-shot tasks

---

## 5. Sub-agents (Task Tool)

Claude can spawn **sub-agents** via the `Task` tool (`AgentTool`):

- Each sub-agent runs its own **nested agentic loop with an isolated conversation**
- Optionally assigned a **restricted tool set** (e.g., read-only tools only)
- Can run locally (in-process) or on remote compute
- Results returned to the parent agent upon completion

This enables **divide-and-conquer** for complex tasks: the parent agent owns the strategy, sub-agents handle individual files or modules.

---

## 6. Conversation Storage & Resumption

### Storage

Conversations are stored as **JSON transcript files** in `~/.claude/`. Each conversation has a unique session ID.

### Resumption

- `--resume <session-id>` — Resume a specific session
- `--resume` (no args) — Pick from a list of previous sessions

### What Happens on Resume

1. **Full message history** loaded from disk
2. **Memory files re-discovered** — May differ from when the conversation first started (files could have been modified/added/deleted)
3. **Permission mode** resets to the configured default (unless persisted in session)

### Compaction — Managing Long Conversations

Long conversations are periodically **compacted** — oldest messages are summarized to keep the context window manageable:

- **Original transcript always preserved on disk** — full integrity maintained
- **Compaction only affects what's sent to the API** — reduces cost and stays within context limits
- This is one of the most critical mechanisms in agent design: how to handle infinite conversations within a finite context window

---

## 7. The Query Engine — Per-Turn Execution

Each "turn" in the agentic loop is driven by a **query** — a call to `query.ts` that sends the current message list to the Anthropic API and streams back the response.

The query engine handles:

1. **Streaming token output** — Real-time display in terminal
2. **`tool_use` block dispatch** — Routes to appropriate tool handlers
3. **Per-turn budget enforcement** — Token count and tool call limits
4. **Tool result collection** — Appends results before the next model call
5. **Compaction trigger** — Fires automatically when context window fills up

### Result Size Limiting (`maxResultSizeChars`)

Each tool has a `maxResultSizeChars` property. When a result exceeds this limit:

1. Full content is **saved to a temporary file**
2. Model receives only a **preview + file path**
3. Prevents context window overflow from large outputs

This ensures that even reading a massive file won't blow up the context.

---

## Architecture Diagram (Conceptual)

```
User Input
    │
    ▼
┌─────────────────────────────────┐
│         Context Assembly         │
│  (git status + CLAUDE.md + date) │
│         [memoized]               │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│        Anthropic API Call        │
│     (query.ts → streaming)       │
└──────────────┬──────────────────┘
               │
          ┌────┴────┐
          │ text?   │ tool_use?
          │         │
          ▼         ▼
     [Response]  ┌──────────────┐
                 │ Permission   │
                 │    Check     │
                 └──────┬───────┘
                   allow│ask│deny
                        │
                        ▼
                 ┌──────────────┐
                 │ Tool Execute │
                 │  + Result    │
                 └──────┬───────┘
                        │
                        ▼
                 [Append to conversation]
                        │
                        ▼
                 [Loop continues ↑]
```

---

## Key Takeaways

### 1. Fully Local Execution

No remote server. Everything runs in the terminal process. This is a security strength — but also means the agent depends on the user's machine resources.

### 2. Compaction Is the Lifeline

How to manage a context window across long conversations is **the** core challenge of agent design. Claude Code's approach:
- Always preserve the original transcript (audit trail)
- Only summarize what's sent to the API
- Also limit individual tool result sizes via `maxResultSizeChars`

### 3. The allow/ask/deny Permission Pattern

This three-tier permission model is becoming the de facto standard for balancing **agent autonomy vs. safety**. Read-only is always allowed, writes depend on mode — simple but effective.

### 4. Sub-agent Pattern as Orchestration Primitive

The Task tool for spawning sub-agents is the foundational pattern for **agent orchestration**. Isolated context + restricted tool set = safe parallel work. This is the starting point for multi-agent systems.
