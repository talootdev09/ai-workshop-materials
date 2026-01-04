# Day 2: n8n Automation

## Overview

Day 2 focuses on building real automations with AI using n8n (no-code workflow automation).

## Learning Goals

- Set up n8n (cloud or local)
- Build visual workflows with AI
- Create real automations (email assistant, document processing)
- Understand when to use no-code vs code

## Structure

### Hour 1: n8n Basics
- Setup n8n
- First workflow: Basic Chatbot
- Compare code vs no-code

### Hour 2: Real Automation
- Build Email AI Assistant
- Integrate with Gmail/Slack

### Hour 3: Document Intelligence
- Build Document Q&A workflow
- Process PDFs and extract information

## Workflows Included

1. **01_basic_chatbot.json** - Simple AI chatbot (Hour 1)
2. **02_email_ai_assistant.json** - Email automation (Hour 2)
3. **03_document_qa.json** - Document Q&A (Hour 3)

## Setup

See `N8N_SETUP_GUIDE.md` for detailed setup instructions.

Quick setup:
```bash
# Option 1: n8n Cloud (recommended for workshop)
# Sign up at: https://n8n.cloud

# Option 2: Local installation
npx n8n
```

## How to Use Workflows

1. Open n8n (cloud or local)
2. Click "Import from File" or "Import from URL"
3. Select the workflow JSON file
4. Configure credentials (OpenAI, Gmail, etc.)
5. Activate and test!

## Workflow Guides

- `WORKFLOW_01_BASIC_CHATBOT.md` - Step-by-step guide
- `WORKFLOW_02_EMAIL_ASSISTANT.md` - Email automation guide
- `WORKFLOW_03_DOCUMENT_QA.md` - Document processing guide

## Tips

- Start with basic chatbot to understand n8n
- Test each node as you build
- Use "Execute Workflow" to test without activating
- Save frequently!

Good luck! 🚀

