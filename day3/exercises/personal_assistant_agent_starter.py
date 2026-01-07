"""
Exercise: Personal Assistant Agent with n8n Integration
======================================================
Build an AI agent that can book meetings and send emails by integrating with n8n workflows.

The agent will:
1. Extract intent and entities from user queries (meeting booking or email sending)
2. Ask for missing information if needed
3. Call n8n webhooks to execute actions (real Google Calendar and Gmail integration)

TODO:
1. Define functions for intent extraction (meeting and email)
2. Define function for triggering n8n webhook
3. Implement agent loop with function calling
4. Handle missing information by asking user
5. Call n8n webhook with structured data
"""

import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# n8n webhook URL - students will configure this after setting up n8n workflow
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "https://your-n8n-instance.com/webhook/personal-assistant")


def trigger_n8n_webhook(action: str, data: dict) -> str:
    """
    Trigger an n8n workflow via webhook.
    
    Args:
        action: The action type ("book_meeting" or "send_email")
        data: Structured data for the action
    
    Returns:
        JSON string with the result from n8n
    """
    try:
        # TODO: Create payload combining action and data
        # Payload should be: {"action": action, **data}
        # This spreads all data fields at the top level (flat structure)
        payload = {
            "action": action,
            **data  # Spread operator combines all data fields
        }
        
        print(f"📤 Sending to n8n: {json.dumps(payload, indent=2)}")
        
        # TODO: Make HTTP POST request to n8n webhook
        # URL: N8N_WEBHOOK_URL
        # Method: POST
        # Headers: {"Content-Type": "application/json"}
        # Body: payload (as JSON)
        # Return the response as JSON string
        
        response = None  # requests.post(N8N_WEBHOOK_URL, json=payload, headers={...}, timeout=30)
        
        # TODO: Check if request was successful
        # response.raise_for_status()
        
        # TODO: Return response as JSON string
        result = None  # response.json()
        print(f"📥 Response from n8n: {json.dumps(result, indent=2) if result else 'No response'}")
        return json.dumps(result) if result else json.dumps({})
    except Exception as e:
        print(f"❌ Error calling n8n: {str(e)}")
        return json.dumps({"status": "error", "message": str(e)})


class PersonalAssistantAgent:
    """An AI agent that can book meetings and send emails via n8n"""
    
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o-mini"
        self.conversation_history = [
            {
                "role": "system",
                "content": """You are a helpful personal assistant that can book meetings and send emails.
                
When users ask to book a meeting:
- Extract: attendee name, email, topic/subject, preferred time, duration
- If time is missing, ask the user for it
- Once you have all required info, use trigger_n8n_webhook with action="book_meeting"

When users ask to send an email:
- Extract: recipient email, subject, message body
- If any info is missing, ask the user
- Once you have all required info, use trigger_n8n_webhook with action="send_email"

Be friendly, ask for missing information clearly, and confirm actions before executing."""
            }
        ]
        
        # TODO: Define functions for the agent
        # You need 3 functions:
        # 1. extract_meeting_intent - Extract meeting booking details
        # 2. extract_email_intent - Extract email sending details  
        # 3. trigger_n8n_webhook - Call n8n workflow
        
        self.functions = [
            # TODO: Function 1: extract_meeting_intent
            # Parameters: attendee_name, attendee_email, topic, preferred_time, duration_minutes
            # Returns structured meeting data
            
            # TODO: Function 2: extract_email_intent
            # Parameters: recipient_email, subject, message
            # Returns structured email data
            
            # TODO: Function 3: trigger_n8n_webhook
            # Parameters: action (string), data (object)
            # This will call the actual n8n webhook
        ]
    
    def execute_function(self, function_name: str, arguments: dict) -> str:
        """Execute a function and return the result"""
        if function_name == "trigger_n8n_webhook":
            # Extract action and data from arguments
            action = arguments.get("action")
            data = arguments.get("data", {})
            
            # If data is empty or None, log warning
            if not data:
                print(f"⚠️  Warning: No data provided for action {action}")
                print(f"   Full arguments: {json.dumps(arguments, indent=2)}")
            
            print(f"🔗 Calling n8n webhook: action={action}")
            print(f"   Data: {json.dumps(data, indent=2)}")
            
            # Call n8n webhook
            result = trigger_n8n_webhook(action, data)
            return result
        else:
            return json.dumps({"status": "error", "message": f"Unknown function: {function_name}"})
    
    def chat(self, user_message: str) -> str:
        """Process user message and handle function calls"""
        # TODO: Add user message to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        max_iterations = 5
        iteration = 0
        
        while iteration < max_iterations:
            iteration += 1
            print(f"\n--- Agent Iteration {iteration} ---")
            
            # TODO: Make API call with functions
            # Include self.functions in the API call
            # Use function_call="auto" to let AI decide when to call functions
            response = None  # client.chat.completions.create(...)
            
            message = response.choices[0].message
            
            # TODO: Check if AI wants to call a function
            if hasattr(message, 'function_call') and message.function_call:
                # TODO: Extract function name and arguments
                function_name = None  # message.function_call.name
                function_args = None  # json.loads(message.function_call.arguments)
                
                print(f"🔧 Agent calling function: {function_name}")
                print(f"   Arguments: {json.dumps(function_args, indent=2)}")
                
                # Execute the function
                function_result = self.execute_function(function_name, function_args)
                print(f"   Result: {function_result[:200]}...")
                
                # TODO: Add assistant's function call to history
                # role="assistant" with function_call
                
                # TODO: Add function result to history
                # role="function" with name=function_name, content=function_result
                
                # Continue loop to let AI process the result
                continue
            else:
                # AI has the final response
                assistant_message = message.content
                self.conversation_history.append({
                    "role": "assistant",
                    "content": assistant_message
                })
                return assistant_message
        
        return "I reached the maximum number of iterations. Please try again with a simpler request."


def main():
    """Run the personal assistant agent"""
    agent = PersonalAssistantAgent()
    
    print("=" * 60)
    print("Personal Assistant Agent")
    print("=" * 60)
    print("\nI can help you:")
    print("  📅 Book meetings (e.g., 'Book a meeting with John about project updates, his email is john@example.com')")
    print("  📧 Send emails (e.g., 'Send an email to sarah@example.com about the meeting tomorrow')")
    print("\nMake sure you've:")
    print("  1. Set up the n8n workflow (import personal_assistant_workflow.json)")
    print("  2. Configured Gmail and Google Calendar credentials in n8n")
    print("  3. Set N8N_WEBHOOK_URL in your .env file")
    print("\n(Type 'quit' to exit)\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("\nPersonal Assistant: Goodbye! 👋")
            break
        
        if not user_input:
            continue
        
        try:
            response = agent.chat(user_input)
            print(f"\nPersonal Assistant: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()

