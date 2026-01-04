"""
Exercise 2: Prompt Engineering Basics
======================================
Learn different techniques to improve prompt quality and control outputs.

TODO:
1. Try a basic prompt without context
2. Add a system message for context
3. Use few-shot prompting with examples
4. Experiment with temperature parameter
5. Request structured output format
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def basic_prompt():
    """Basic prompt without much context"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # TODO: Make a simple API call
    # Model: "gpt-4o-mini"
    # User message: "Explain what a variable is in programming"
    response = None
    
    print("=== Basic Prompt ===")
    print("YOUR_CODE_HERE")
    print("\n")


def prompt_with_context():
    """Add a system message to give the AI a role/context"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # TODO: Add a system message
    # System: "You are a friendly teacher explaining programming concepts to beginners. Use simple language and real-world analogies."
    # User: "Explain what a variable is in programming"
    response = None
    
    print("=== Prompt with Context ===")
    print("YOUR_CODE_HERE")
    print("\n")


def prompt_with_examples():
    """Use few-shot prompting with examples"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # TODO: Create a conversation with examples
    # System: "You explain programming concepts using creative analogies."
    # User: "What is a function?"
    # Assistant: "A function is like a recipe in a cookbook..."
    # User: "What is a loop?"
    response = None
    
    print("=== Prompt with Examples (Few-shot) ===")
    print("YOUR_CODE_HERE")
    print("\n")


def temperature_experiment():
    """Experiment with temperature parameter"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = "Write a creative opening line for a sci-fi story"
    
    # TODO: Make two calls with different temperatures
    # One with temperature=0.2 (low, more deterministic)
    # One with temperature=1.5 (high, more creative)
    response_low = None
    response_high = None
    
    print("=== Temperature Experiment ===")
    print("Low temperature (0.2) - More focused:")
    print("YOUR_CODE_HERE")
    print("\nHigh temperature (1.5) - More creative:")
    print("YOUR_CODE_HERE")
    print("\n")


def structured_output_example():
    """Bonus: Request structured output format"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # TODO: Request JSON format output
    # System: "You provide responses in JSON format."
    # User: "List 3 benefits of using functions in programming. Format as JSON with 'benefits' array."
    response = None
    
    print("=== Structured Output ===")
    print("YOUR_CODE_HERE")
    print("\n")


if __name__ == "__main__":
    print("Running prompt engineering examples...\n")
    basic_prompt()
    prompt_with_context()
    prompt_with_examples()
    temperature_experiment()
    structured_output_example()

