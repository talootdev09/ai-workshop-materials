# Day 3: Agentic AI - AI Agents That Think and Act

## Overview

Day 3 focuses on building AI agents - intelligent systems that can reason, plan, and use tools to accomplish tasks autonomously.

## Learning Goals

- Understand what AI agents are and how they differ from chatbots
- Learn function calling / tool use with OpenAI
- Build agents that can use tools and make decisions
- Understand agent patterns (planning, execution, reflection)
- Create multi-step reasoning agents

## Structure

### Hour 1: Understanding AI Agents (Conceptual + Intro)
- What are AI agents?
- Agents vs chatbots
- Core concepts: planning, tool use, memory
- Real-world examples

### Hour 2: Building Your First Agent
- Function calling / tool use
- OpenAI function calling API
- Exercise 1: Basic Function Calling
- Exercise 2: Calculator Agent

### Hour 3: Advanced Agent Patterns
- Multi-step reasoning
- Agent loops (plan → execute → reflect)
- Exercise 3: Research Assistant Agent
- Error handling and recovery

### Hour 4: Real Applications & Day 4 Prep
- Building complete agent applications
- Combining agents with n8n
- Agent project ideas for Day 4

## Exercises

### Exercise 1: Basic Function Calling
**File**: `exercises/01_basic_function_calling_starter.py`

**Learning Goals**:
- Understand function calling API
- Define tools/functions for AI
- Handle function calls and responses

**Time**: 30 minutes

### Exercise 2: Calculator Agent
**File**: `exercises/02_calculator_agent_starter.py`

**Learning Goals**:
- Build a simple agent with tools
- Implement tool execution
- Handle multi-step calculations

**Time**: 40 minutes

### Exercise 3: Research Assistant Agent
**File**: `exercises/03_research_agent_starter.py`

**Learning Goals**:
- Multi-step reasoning
- Agent loops (plan → execute → reflect)
- Build a research assistant that can search and summarize

**Time**: 50 minutes

### Exercise 4: Task Automation Agent (Bonus)
**File**: `exercises/04_task_automation_agent_starter.py`

**Learning Goals**:
- Advanced agent patterns
- Error handling and recovery
- Complex multi-step task planning

**Time**: Optional (if ahead of schedule)

## Setup

1. **Install dependencies**:
```bash
pip install openai python-dotenv requests
```

2. **Set up API key**:
- Use your existing OpenAI API key from Day 1
- Or get one from OpenRouter.ai

3. **Run exercises**:
```bash
cd day3/exercises
python 01_basic_function_calling_starter.py
```

## Key Concepts

### Function Calling
- AI can request to call functions
- You define available tools
- AI decides when to use them
- You execute and return results

### Agent Patterns
1. **Planning**: Agent breaks down task into steps
2. **Execution**: Agent calls tools to complete steps
3. **Reflection**: Agent evaluates progress and adjusts

### Tool Use
- Calculator functions
- Web search (simulated)
- File operations
- API calls
- Database queries

## Solutions

All solutions are in the `solutions/` folder. Compare your code with the solutions to see different approaches and best practices.

## Next Steps

After Day 3, you'll be ready for Day 4: Student Projects, where you can build:
- Personal assistant agents
- Research agents
- Code generation agents
- Customer service agents
- Workflow automation agents

Good luck! 🚀
