"""
Exercise 3: Building a Chatbot with Conversation Memory - SOLUTION
===================================================================
A complete chatbot implementation with conversation memory.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json

load_dotenv()

class SimpleChatbot:
    """A simple chatbot with conversation memory"""
    
    def __init__(self, system_prompt="You are a helpful assistant."):
        """Initialize the chatbot with a system prompt"""
        # self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o-mini"
        self.api_key = os.getenv("OPENAI_API_KEY")
        
        # Initialize conversation history with system message
        self.conversation_history = [
            {"role": "system", "content": system_prompt}
        ]
    
    def chat(self, user_message):
        """Send a message and get a response"""
        
        # Add user message to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Send conversation history to API
        # response = self.client.chat.completions.create(
        #     model=self.model,
        #     messages=self.conversation_history
        # )
        
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
            },
            data=json.dumps({
                "model": self.model,
                "messages": self.conversation_history
            })
        )
        # Extract assistant's response
        assistant_message = response.json()["choices"][0]["message"]["content"]
        
        # Add assistant's response to conversation history
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def get_history(self):
        """Return the conversation history (for debugging)"""
        return self.conversation_history
    
    def clear_history(self, keep_system=True):
        """Clear conversation history"""
        if keep_system and self.conversation_history:
            system_msg = self.conversation_history[0]
            self.conversation_history = [system_msg]
        else:
            self.conversation_history = []


def main():
    """Run the chatbot in a loop"""
    
    # Create a chatbot with a custom personality
    chatbot = SimpleChatbot(
        system_prompt="You are a friendly Python programming tutor. Keep responses concise and encouraging."
    )
    
    print("Chatbot: Hello! I'm your Python tutor. Ask me anything about Python!")
    print("(Type 'quit' to exit, 'history' to see conversation, 'clear' to reset)\n")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! Happy coding!")
            break
        
        if user_input.lower() == 'history':
            print("\n=== Conversation History ===")
            for msg in chatbot.get_history():
                role = msg['role'].capitalize()
                content = msg['content']
                print(f"{role}: {content}")
                print("-" * 50)
            print("============================\n")
            continue
        
        if user_input.lower() == 'clear':
            chatbot.clear_history()
            print("Chatbot: Conversation cleared! Let's start fresh.\n")
            continue
        
        if not user_input:
            continue
        
        try:
            # Get chatbot response
            response = chatbot.chat(user_input)
            print(f"Chatbot: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()

