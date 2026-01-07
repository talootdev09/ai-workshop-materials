# Day 3: Agentic AI - AI Agents That Think and Act

## Overview

Day 3 focuses on building AI agents - intelligent systems that can reason, plan, and use tools to accomplish tasks autonomously. You'll build a **Personal Assistant Agent** that integrates with n8n to book meetings and send emails.

## Learning Goals

- Understand what AI agents are and how they differ from chatbots
- Learn function calling / tool use with OpenAI
- Build agents that can use tools and make decisions
- Understand agent patterns (planning, execution, reflection)
- Integrate agents with n8n workflows for real-world automation
- Create multi-step reasoning agents

## Structure

### Hour 1: Understanding AI Agents (Conceptual)
- What are AI agents?
- Agents vs chatbots
- Core concepts: planning, tool use, memory
- Real-world examples
- Business value of agents

### Hour 2: Function Calling & Agent Basics
- Function calling / tool use
- OpenAI function calling API
- How agents decide when to use tools
- Building the foundation

### Hour 3: Building Your Personal Assistant Agent
- **Exercise: Personal Assistant Agent with n8n Integration**
- Intent extraction and entity recognition
- Multi-step reasoning
- Agent loops (plan → execute → reflect)
- Integrating with n8n workflows

### Hour 4: Real Applications & Day 4 Prep
- Building complete agent applications
- Combining agents with n8n
- Agent project ideas for Day 4

## Exercise: Personal Assistant Agent

### Overview
Build an AI agent that can:
- 📅 **Book meetings** - Creates real Google Calendar events
- 📧 **Send emails** - Sends real emails via Gmail

The agent uses function calling to extract intent and entities, then triggers n8n workflows for execution.

### Files
- **Starter Code:** `exercises/personal_assistant_agent_starter.py`
- **Solution:** `solutions/personal_assistant_agent_solution.py`
- **n8n Workflow:** `../day2/workflows/personal_assistant_workflow.json`
- **Setup Guide:** `PERSONAL_ASSISTANT_SETUP.md`
- **Quick Reference:** `README_PERSONAL_ASSISTANT.md`

### Learning Goals
- ✅ Understand function calling with multiple tools
- ✅ Extract intent and entities from natural language
- ✅ Handle missing information (ask user)
- ✅ Integrate agents with n8n workflows
- ✅ Multi-step reasoning and agent loops
- ✅ Real-world application (actual calendar events and emails)

### Time: 90 minutes

### Prerequisites
1. ✅ Completed Day 1 (API calls)
2. ✅ Completed Day 2 (n8n basics)
3. ✅ OpenAI API key (in `.env` file)
4. ✅ n8n instance (cloud or local)
5. ✅ Gmail account (for email sending)
6. ✅ Google Calendar access (for meeting booking)

### Quick Start

1. **Set up n8n workflow** (15 min)
   - Import `day2/workflows/personal_assistant_workflow.json`
   - Configure Google Calendar OAuth2 credential
   - Configure Gmail OAuth2 credential
   - Activate workflow and copy webhook URL

2. **Configure agent** (5 min)
   - Add `N8N_WEBHOOK_URL` to `.env` file
   - Install: `pip install requests`

3. **Build the agent** (60 min)
   - Complete TODOs in `personal_assistant_agent_starter.py`
   - Test with example queries

4. **Test and iterate** (10 min)
   - Try booking meetings
   - Try sending emails
   - See real results!

### Example Usage

**Book Meeting:**
```
You: Book the meeting with John about his falling stats, his email is John@gmail.com
Agent: What time would you like to schedule this meeting?
You: Tuesday 2pm
Agent: Done! Meeting scheduled for Tuesday at 2pm. Calendar invite sent to John@gmail.com.
```

**Send Email:**
```
You: Send an email to sarah@example.com about the meeting tomorrow
Agent: What should the subject be? And what message?
You: Subject: Meeting Tomorrow, Message: Don't forget our meeting at 2pm
Agent: Email sent successfully to sarah@example.com!
```

## Setup

1. **Install dependencies**:
```bash
pip install openai python-dotenv requests
```

2. **Set up API key**:
- Use your existing OpenAI API key from Day 1
- Add to `.env`: `OPENAI_API_KEY=your_key_here`

3. **Set up n8n**:
- Follow `PERSONAL_ASSISTANT_SETUP.md` for detailed instructions
- Import workflow and configure credentials
- Add webhook URL to `.env`: `N8N_WEBHOOK_URL=https://your-n8n.com/webhook/personal-assistant`

4. **Run the exercise**:
```bash
cd day3/exercises
python personal_assistant_agent_starter.py
```

## Key Concepts

### Function Calling
- AI can request to call functions you define
- You describe available tools (name, parameters, description)
- AI decides when to use them
- You execute and return results

### Agent Patterns
1. **Planning**: Agent breaks down task into steps
2. **Execution**: Agent calls tools to complete steps
3. **Reflection**: Agent evaluates progress and adjusts

### Agent + n8n Integration
- **Agent (Python)**: Handles reasoning, intent extraction, entity extraction
- **n8n (Workflow)**: Handles execution, integrations (Gmail, Calendar)
- **Best of both worlds**: Smart reasoning + reliable automation

## Architecture

```
User Query
    ↓
Python Agent (function calling)
    ↓
Agent extracts: intent + entities
    ↓
Agent asks for missing info (if needed)
    ↓
Agent calls n8n webhook with structured data
    ↓
n8n workflow executes (creates calendar event, sends email)
    ↓
Agent returns result to user
```

## Success Criteria

✅ Agent extracts intent correctly (meeting vs email)  
✅ Agent extracts all entities (emails, names, topics, etc.)  
✅ Agent asks for missing information  
✅ Agent calls n8n webhook with structured data  
✅ n8n creates real calendar events  
✅ n8n sends real emails  
✅ Agent returns results to user  

## Next Steps

After Day 3, you'll be ready for Day 4: Student Projects, where you can build:
- Enhanced personal assistant agents
- Research agents
- Code generation agents
- Customer service agents
- Workflow automation agents
- Your own custom agent!

Good luck! 🚀
