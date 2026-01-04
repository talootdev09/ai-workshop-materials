# 9-Hour AI Workshop - Complete Materials

Complete coding exercises and solutions for the 4-day AI workshop.

## 📁 Structure

```
9hour_workshop_complete/
├── day1/                    # Day 1: LLM APIs & Code Basics
│   ├── exercises/          # Student exercises (TODO items)
│   ├── solutions/          # Complete solutions
│   └── bonus/              # Optional streaming exercise
│
├── day2/                    # Day 2: n8n Automation
│   ├── workflows/          # n8n workflow JSON files
│   ├── N8N_SETUP_GUIDE.md  # n8n setup instructions
│   ├── WORKFLOW_*.md       # Step-by-step workflow guides
│   └── test_*.html         # Webhook test pages
│
├── day3/                    # Day 3: Agentic AI
│   ├── exercises/          # Student exercises (function calling, agents)
│   └── solutions/          # Complete solutions
│
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Add your OpenAI API key to .env
# OPENAI_API_KEY=your_key_here
```

### 2. Day 1 Exercises

**Exercise 1: First API Call**
```bash
cd day1/exercises
python 01_first_api_call_starter.py
# Compare with: ../solutions/01_first_api_call_solution.py
```

**Exercise 2: Prompt Engineering**
```bash
python 02_prompt_engineering_starter.py
# Compare with: ../solutions/02_prompt_engineering_solution.py
```

**Exercise 3: Chatbot with Memory**
```bash
python 03_chatbot_memory_starter.py
# Compare with: ../solutions/03_chatbot_memory_solution.py
```

**Bonus: Streaming**
```bash
cd ../bonus
python 04_streaming_bonus.py
```

### 2. Day 2: n8n Workflows

**Setup n8n**:
- Option 1: Sign up at https://n8n.cloud (recommended)
- Option 2: Run `npx n8n` locally
- See `day2/N8N_SETUP_GUIDE.md` for details

**Workflow 1: Basic Chatbot**
1. Import `day2/workflows/01_basic_chatbot.json`
2. Configure OpenAI credential
3. Activate workflow
4. Test with `day2/test_webhook_chatbot.html`

**Workflow 2: Email AI Assistant**
1. Import `day2/workflows/02_email_ai_assistant.json`
2. Configure Gmail OAuth
3. Activate and test with real email

**Workflow 3: Document Q&A**
1. Import `day2/workflows/03_document_qa.json`
2. Test with `day2/test_webhook_document.html`

**See**: `day2/WORKFLOW_*.md` for step-by-step guides

### 3. Day 3: Agentic AI Exercises

**Exercise 1: Basic Function Calling**
```bash
cd day3/exercises
python 01_basic_function_calling_starter.py
# Compare with: ../solutions/01_basic_function_calling_solution.py
```

**Exercise 2: Calculator Agent**
```bash
python 02_calculator_agent_starter.py
# Compare with: ../solutions/02_calculator_agent_solution.py
```

**Exercise 3: Research Assistant Agent**
```bash
python 03_research_agent_starter.py
# Compare with: ../solutions/03_research_agent_solution.py
```

**Exercise 4: Task Automation Agent (Bonus)**
```bash
python 04_task_automation_agent_starter.py
# Compare with: ../solutions/04_task_automation_agent_solution.py
```

**See**: `day3/README.md` for detailed instructions

## 📚 Day-by-Day Guide

### Day 1: LLM APIs & Code Basics (3 hours)

**Hour 1: Setup & First Success**
- Exercise 1: First API Call
- Goal: Everyone makes a successful API call

**Hour 2: Prompt Engineering**
- Exercise 2: Prompt Engineering
- Topics: System messages, temperature, few-shot learning

**Hour 3: Chatbot with Memory**
- Exercise 3: Chatbot with Memory
- Build a working chatbot that remembers context

### Day 2: n8n Automation (3 hours)

**Hour 1: n8n Basics**
- Setup n8n (cloud or local)
- First workflow: Basic Chatbot
- Compare code vs no-code

**Hour 2: Real Automation**
- Build Email AI Assistant
- Gmail integration
- Auto-analyze and draft responses

**Hour 3: Document Intelligence**
- Build Document Q&A workflow
- Process PDFs
- Extract and answer questions

**See**: `day2/README.md` for detailed instructions

### Day 3: Agentic AI - AI Agents That Think and Act (3 hours)

**Hour 1: Understanding AI Agents**
- What are AI agents?
- Agents vs chatbots
- Core concepts: planning, tool use, memory

**Hour 2: Building Your First Agent**
- Function calling / tool use
- Exercise 1: Basic Function Calling
- Exercise 2: Calculator Agent

**Hour 3: Advanced Agent Patterns**
- Multi-step reasoning
- Agent loops (plan → execute → reflect)
- Exercise 3: Research Assistant Agent
- Exercise 4: Task Automation Agent (bonus)

**See**: `day3/README.md` for detailed instructions

## 🎯 Learning Objectives

By the end of the workshop, students will:
- ✅ Make LLM API calls
- ✅ Build a chatbot with memory
- ✅ Understand prompt engineering basics
- ✅ Create n8n workflows for automation
- ✅ Build real automations (email, documents)
- ✅ Understand AI agents and function calling
- ✅ Build agents that can use tools and make decisions
- ✅ Create multi-step reasoning agents

## 📝 Notes for Instructors

- **Exercises** folder contains starter code with TODOs
- **Solutions** folder has complete working code
- Students should try exercises first, then check solutions
- All code is tested and ready to run

## 🔧 Troubleshooting

**API Key Issues**
- Make sure `.env` file exists and has `OPENAI_API_KEY`
- Check key is valid at https://platform.openai.com

**Import Errors**
- Run `pip install -r requirements.txt`
- Make sure you're in the correct directory

**FastAPI Issues**
- Install uvicorn: `pip install uvicorn`
- Run with: `uvicorn main:app --reload`

## 📖 Additional Resources

- OpenAI API Docs: https://platform.openai.com/docs
- FastAPI Docs: https://fastapi.tiangolo.com
- Python Best Practices: https://docs.python.org/3/tutorial/

---

**Happy Coding! 🚀**

