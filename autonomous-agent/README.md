# Autonomous LangChain Agent System (Fully Local)

A fully local autonomous AI agent capable of reasoning step-by-step, dynamically selecting tools, maintaining short-term memory, and producing structured JSON outputs.

The system runs entirely on local models using Ollama and does not rely on any paid APIs.

---

## Overview

This project implements a loop-based autonomous agent architecture with:

- Step-by-step reasoning
- Dynamic tool selection
- Execution limits to prevent infinite loops
- Structured JSON output enforcement
- Short-term conversational memory
- Local model inference

The agent operates using an iterative reasoning loop and executes tools based on model decisions.

---

## Tech Stack

| Component            | Technology Used |
|----------------------|----------------|
| LLM                  | Llama 3 (Ollama) |
| Agent Framework      | Custom loop-based design |
| Tool Execution       | Python execution, Web search, File writing |
| Memory               | Sliding window short-term memory |
| Output Validation    | JSON parsing + schema enforcement |
| Runtime              | Fully local |

---

## Project Structure

---

## Agent Workflow

1. User provides a task.
2. Agent generates structured reasoning in JSON format.
3. Agent selects a tool (or finishes).
4. Tool executes and returns output.
5. Tool output is added to memory.
6. Loop continues until:
   - Task is complete
   - Iteration limit is reached

---

## Engineering Controls

### Tool Selection Safety
- Only predefined tool names are allowed.
- Invalid tool names are handled gracefully.

### Infinite Loop Prevention
- Hard iteration limit enforced (`MAX_ITERATIONS`).
- Agent stops automatically if limit is reached.

### Memory Control
- Sliding window memory prevents unbounded growth.
- Old messages are discarded after threshold.

### Output Reliability
- JSON-only response requirement.
- Regex-based JSON extraction.
- Validation before execution.

### Tool Output Management
- Tool outputs are truncated to prevent context overflow.

---

## Running the Agent

Ensure Ollama is installed and Llama 3 is pulled:

Enter a task when prompted.

Example tasks:

- `Calculate 10 factorial using python`
- `Research the current GDP of Germany and summarize`
- `Write a short report about AI to report.txt`

---

## Design Decisions

- Loop-based agent architecture instead of black-box frameworks
- Explicit tool control to reduce hallucinated tool calls
- Local-only inference for independence and reproducibility
- Structured output enforcement for predictable behavior

---

## What This Project Demonstrates

- Autonomous reasoning loop implementation
- Tool orchestration and execution control
- Failure handling and guardrails
- Memory management strategy
- Structured LLM output enforcement
- Local AI system design
