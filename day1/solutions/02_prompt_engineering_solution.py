"""
Exercise 2: Prompt Engineering Basics - SOLUTION
=================================================
Different techniques to improve prompt quality and control outputs.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json

load_dotenv()

def basic_prompt():
    """Basic prompt without much context"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "user", "content": "Explain what a variable is in programming"}
    #     ]
    # )
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        },
        data=json.dumps({
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "user", "content": "Explain what a variable is in programming"}
            ]
        })
    )
    response = response.json()["choices"][0]["message"]["content"]    
    print("=== Basic Prompt ===")
    print(response)
    print("\n")


def prompt_with_context():
    """Add a system message to give the AI a role/context"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": "You are a friendly teacher explaining programming concepts to beginners. Use simple language and real-world analogies."},
    #         {"role": "user", "content": "Explain what a variable is in programming"}
    #     ]
    # )
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        },
        data=json.dumps({
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are a friendly teacher explaining programming concepts to beginners. Use simple language and real-world analogies."},
                {"role": "user", "content": "Explain what a variable is in programming"}
            ]
        })
    )
    print("=== Prompt with Context ===")
    print(response.json()["choices"][0]["message"]["content"])
    print("\n")


def prompt_with_examples():
    """Use few-shot prompting with examples"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": "You explain programming concepts using creative analogies."},
    #         {"role": "user", "content": "What is a function?"},
    #         {"role": "assistant", "content": "A function is like a recipe in a cookbook. You give it ingredients (inputs), it follows a set of instructions, and produces a dish (output). Just like you can use the same recipe multiple times with different ingredients, you can call a function multiple times with different inputs."},
    #         {"role": "user", "content": "What is a loop?"}
    #     ]
    # )
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        },
        data=json.dumps({
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You explain programming concepts using creative analogies."},
                {"role": "user", "content": "What is a function?"},
                {"role": "assistant", "content": "A function is like a recipe in a cookbook. You give it ingredients (inputs), it follows a set of instructions, and produces a dish (output). Just like you can use the same recipe multiple times with different ingredients, you can call a function multiple times with different inputs."},
                {"role": "user", "content": "What is a loop?"}
            ]
        })
    )
    print("=== Prompt with Examples (Few-shot) ===")
    print(response.json()["choices"][0]["message"]["content"])
    print("\n")


def temperature_experiment():
    """Experiment with temperature parameter"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = "Write a creative opening line for a sci-fi story"
    
    # Low temperature (more deterministic, focused)
    # response_low = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[{"role": "user", "content": prompt}],
    #     temperature=0.2
    # )
    
    # # High temperature (more creative, random)
    # response_high = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[{"role": "user", "content": prompt}],
    #     temperature=1.5
    # )

    response_low = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        },
        data=json.dumps({
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        })
    )
    response_high = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        },
        data=json.dumps({
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 1.5
        })
    )
    print("=== Temperature Experiment ===")
    print("Low temperature (0.2) - More focused:")
    print(response_low.json()["choices"][0]["message"]["content"])
    print("\nHigh temperature (1.5) - More creative:")
    print(response_high.json()["choices"][0]["message"]["content"])
    print("\n")


def structured_output_example():
    """Bonus: Request structured output format"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": "You provide responses in JSON format."},
    #         {"role": "user", "content": "List 3 benefits of using functions in programming. Format as JSON with 'benefits' array."}
    #     ]
    # )

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        },
        data=json.dumps({
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You provide responses in JSON format."},
                {"role": "user", "content": "List 3 benefits of using functions in programming. Format as JSON with 'benefits' array."}
            ]
        })
    )
    print("=== Structured Output ===")
    print(response.json()["choices"][0]["message"]["content"])
    print("\n")


if __name__ == "__main__":
    print("Running prompt engineering examples...\n")
    basic_prompt()
    prompt_with_context()
    prompt_with_examples()
    temperature_experiment()
    structured_output_example()

