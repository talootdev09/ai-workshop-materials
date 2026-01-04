# Setup Guide for 9-Hour Workshop

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key (get from https://platform.openai.com/api-keys)

## Step-by-Step Setup

### 1. Clone/Navigate to Workshop Folder

```bash
cd workshop
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
# OPENAI_API_KEY=sk-your-actual-key-here
```

**How to get OpenAI API Key:**
1. Go to https://platform.openai.com
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new secret key
5. Copy it to your `.env` file

### 5. Verify Setup

```bash
# Test Day 1 Exercise 1
cd day1/solutions
python 01_first_api_call_solution.py
```

If you see an AI response, setup is complete! ✅

## Troubleshooting

### "Module not found" errors
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

### "OPENAI_API_KEY not found" error
- Check `.env` file exists in root directory
- Verify API key is correct (starts with `sk-`)
- Make sure no extra spaces in `.env` file

### API Key errors
- Verify key is valid at https://platform.openai.com
- Check you have credits in your OpenAI account
- Ensure key has proper permissions


## Next Steps

1. Complete Day 1 exercises (start with `exercises/` folder)
2. Check solutions when stuck
3. Try Day 4 projects when ready

Good luck! 🚀

