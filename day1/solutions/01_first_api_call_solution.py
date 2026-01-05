"""
Exercise 1: Your First LLM API Call - SOLUTION
===============================================
This is the complete solution for making your first API call.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json

# Load environment variables from .env file
load_dotenv()

def first_api_call():
    """Make your first API call to an LLM"""
    
    # Get the API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file")
        return
    
    # Create an OpenAI client
    #client = OpenAI(api_key=api_key)
    # client = OpenAI(
    #     base_url="openrouter.ai", 
    #     api_key=api_key)
    
    # # Make an API call
    # response = client.chat.completions.create(
    #     #model="gpt-4o-mini",
    #     model="google/gemma-2-9b-it",
    #     messages=[
    #         {"role": "user", "content": "Say hello and introduce yourself in one sentence!"}
    #     ]
    # )

    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
    },
    data=json.dumps({
        "model": "openai/gpt-4o-mini-2024-07-18", # Optional
        "messages": [
        {
            "role": "user",
            "content": "Say hello and introduce yourself in one sentence!"
        }
        ]
    })
    )
    
    # Extract and print the response
    #ai_message = response.choices[0].message.content
    ai_message = response.json()["choices"][0]["message"]["content"]
    print("AI Response:", ai_message)
    
    # Bonus: Print some metadata
    #print(f"\nTokens used: {response.usage.total_tokens}")
    print(f"\nTokens used: {response.json()['usage']['total_tokens']}")
    #print(f"Model: {response.model}")
    print(f"Model: {response.json()['model']}")


if __name__ == "__main__":
    first_api_call()

