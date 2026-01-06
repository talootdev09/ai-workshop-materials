"""
Bonus Exercise: Streaming Responses
====================================
Make responses appear word-by-word like ChatGPT!

This creates a better user experience for longer responses.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class StreamingChatbot:
    """A chatbot that streams responses in real-time"""
    
    def __init__(self, system_prompt="You are a helpful assistant."):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o-mini"
        self.conversation_history = [
            {"role": "system", "content": system_prompt}
        ]
    
    def chat_streaming(self, user_message):
        """Send a message and stream the response"""
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Create streaming request (note: stream=True)
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            stream=True  # Enable streaming!
        )
        
        # Collect the full response while streaming
        full_response = ""
        
        print("Chatbot: ", end="", flush=True)
        
        # Process each chunk as it arrives
        for chunk in stream:
            # Extract content from chunk
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_response += content
                print(content, end="", flush=True)
        
        print()  # New line after response
        
        # Add complete response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": full_response
        })
        
        return full_response


def main():
    """Run the streaming chatbot"""
    
    chatbot = StreamingChatbot(
        system_prompt="You are a helpful assistant who explains things clearly."
    )
    
    print("Streaming Chatbot Ready! Watch responses appear in real-time.")
    print("(Type 'quit' to exit)\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        
        if not user_input:
            continue
        
        try:
            chatbot.chat_streaming(user_input)
            print()  # Extra line for spacing
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()

