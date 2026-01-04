"""
Exercise 1: Your First LLM API Call
====================================
In this exercise, you'll make your first call to an LLM API.

TODO:
1. Load your API key from the .env file
2. Create a client instance
3. Send a simple prompt to the API
4. Print the response

Run this file with: python 01_first_api_call_starter.py
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

def first_api_call():
    """Make your first API call to an LLM"""
    
    # TODO: Get the API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file")
        return
    
    # TODO: Create an OpenAI client
    # Hint: client = OpenAI(api_key=api_key)
    client = None
    
    # TODO: Make an API call
    # Hint: Use client.chat.completions.create()
    # Model: "gpt-4o-mini"
    # Messages: [{"role": "user", "content": "Say hello and introduce yourself in one sentence!"}]
    response = None
    
    # TODO: Extract and print the response
    # Hint: response.choices[0].message.content
    print("AI Response:", "YOUR_CODE_HERE")


if __name__ == "__main__":
    first_api_call()

