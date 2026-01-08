"""
Exercise: Personal Assistant Agent with n8n Integration - SOLUTION (OpenRouter)
================================================================================
Complete solution for the personal assistant agent that integrates with n8n.
This version uses OpenRouter AI instead of OpenAI.
"""

import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# n8n webhook URL - configure this after setting up n8n workflow
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
        # Combine action and data into flat payload
        payload = {
            "action": action,
            **data  # Spread data fields at top level
        }
        
        print(f"📤 Sending to n8n: {json.dumps(payload, indent=2)}")
        
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        print(f"📥 Response from n8n: {json.dumps(result, indent=2)}")
        return json.dumps(result)
    except requests.exceptions.RequestException as e:
        error_msg = f"Failed to call n8n: {str(e)}"
        print(f"❌ Error: {error_msg}")
        return json.dumps({"status": "error", "message": error_msg})
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Error: {error_msg}")
        return json.dumps({"status": "error", "message": error_msg})


class PersonalAssistantAgent:
    """An AI agent that can book meetings and send emails via n8n"""
    
    def __init__(self):
        # Initialize OpenRouter client
        # OpenRouter uses OpenAI-compatible API with custom base_url
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
        # You can use any model available on OpenRouter
        # Examples: "openai/gpt-4o-mini", "anthropic/claude-3-haiku", "google/gemini-pro"
        self.model = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")
        
        self.conversation_history = [
            {
                "role": "system",
                "content": """You are a helpful personal assistant that can book meetings and send emails.
                
When users ask to book a meeting:
- Extract: attendee name, email, topic/subject, preferred time, duration
- If time is missing, ask the user for it
- Once you have all required info, use trigger_n8n_webhook with action="book_meeting"
- IMPORTANT: When calling trigger_n8n_webhook, the 'data' parameter must be a flat object containing all meeting details:
  Example: {"action": "book_meeting", "data": {"attendee_email": "john@example.com", "attendee_name": "John", "topic": "project update", "preferred_time": "Tuesday 2pm", "duration_minutes": 30}}

When users ask to send an email:
- Extract: recipient email, subject, message body
- If any info is missing, ask the user
- Once you have all required info, use trigger_n8n_webhook with action="send_email"
- IMPORTANT: When calling trigger_n8n_webhook, the 'data' parameter must be a flat object containing all email details:
  Example: {"action": "send_email", "data": {"recipient_email": "sarah@example.com", "subject": "Meeting tomorrow", "message": "Don't forget our meeting at 2pm"}}

Be friendly, ask for missing information clearly, and confirm actions before executing."""
            }
        ]
        
        # Define tools for the agent (OpenRouter uses 'tools' format instead of 'functions')
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "extract_meeting_intent",
                    "description": "Extract meeting booking details from user query. Use this when user wants to schedule or book a meeting.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "attendee_name": {
                                "type": "string",
                                "description": "Name of the person to meet with"
                            },
                            "attendee_email": {
                                "type": "string",
                                "description": "Email address of the attendee"
                            },
                            "topic": {
                                "type": "string",
                                "description": "Subject or topic of the meeting"
                            },
                            "preferred_time": {
                                "type": "string",
                                "description": "Preferred time for the meeting (e.g., 'Tuesday 2pm', 'next week Monday', 'tomorrow at 3pm'). Leave as null if not specified."
                            },
                            "duration_minutes": {
                                "type": "integer",
                                "description": "Duration of the meeting in minutes. Default to 30 if not specified.",
                                "default": 30
                            }
                        },
                        "required": ["attendee_email", "topic"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "extract_email_intent",
                    "description": "Extract email sending details from user query. Use this when user wants to send an email.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "recipient_email": {
                                "type": "string",
                                "description": "Email address of the recipient"
                            },
                            "subject": {
                                "type": "string",
                                "description": "Subject line of the email"
                            },
                            "message": {
                                "type": "string",
                                "description": "Body/content of the email message"
                            }
                        },
                        "required": ["recipient_email", "subject", "message"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "trigger_n8n_webhook",
                    "description": "Trigger an n8n automation workflow to execute an action (book meeting or send email). Use this after extracting all required information. IMPORTANT: The 'data' parameter must contain all the meeting or email details as a flat object (not nested).",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "action": {
                                "type": "string",
                                "enum": ["book_meeting", "send_email"],
                                "description": "The action to perform: 'book_meeting' or 'send_email'"
                            },
                            "data": {
                                "type": "object",
                                "description": "Structured data for the action. For book_meeting: MUST include attendee_email, topic, and preferred_time. Optionally include attendee_name and duration_minutes. For send_email: MUST include recipient_email, subject, and message. Pass all fields as a flat object, e.g. {'attendee_email': 'john@example.com', 'topic': 'meeting', 'preferred_time': 'Tuesday 2pm'}",
                                "properties": {
                                    "attendee_email": {"type": "string", "description": "Email of meeting attendee (for book_meeting)"},
                                    "attendee_name": {"type": "string", "description": "Name of meeting attendee (for book_meeting)"},
                                    "topic": {"type": "string", "description": "Meeting topic/subject (for book_meeting)"},
                                    "preferred_time": {"type": "string", "description": "Preferred meeting time (for book_meeting)"},
                                    "duration_minutes": {"type": "integer", "description": "Meeting duration in minutes (for book_meeting)"},
                                    "recipient_email": {"type": "string", "description": "Email recipient (for send_email)"},
                                    "subject": {"type": "string", "description": "Email subject (for send_email)"},
                                    "message": {"type": "string", "description": "Email message body (for send_email)"}
                                }
                            }
                        },
                        "required": ["action", "data"]
                    }
                }
            }
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
        elif function_name == "extract_meeting_intent":
            # Just return the extracted data - agent will decide if it needs to call n8n
            return json.dumps({"status": "extracted", "data": arguments})
        elif function_name == "extract_email_intent":
            # Just return the extracted data - agent will decide if it needs to call n8n
            return json.dumps({"status": "extracted", "data": arguments})
        else:
            return json.dumps({"status": "error", "message": f"Unknown function: {function_name}"})
    
    def chat(self, user_message: str) -> str:
        """Process user message and handle tool calls"""
        # Add user message to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        max_iterations = 5
        iteration = 0
        
        while iteration < max_iterations:
            iteration += 1
            print(f"\n--- Agent Iteration {iteration} ---")
            
            # Make API call with tools (OpenRouter uses 'tools' instead of 'functions')
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                tools=self.tools,
                tool_choice="auto"  # OpenRouter uses 'tool_choice' instead of 'function_call'
            )
            
            message = response.choices[0].message
            
            # Check if AI wants to call a tool (OpenRouter uses 'tool_calls' instead of 'function_call')
            if message.tool_calls:
                # OpenRouter returns tool_calls as a list, so we need to handle each one
                for tool_call in message.tool_calls:
                    # Extract function name and arguments
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)
                    tool_call_id = tool_call.id
                    
                    print(f"🔧 Agent calling function: {function_name}")
                    print(f"   Arguments: {json.dumps(function_args, indent=2)}")
                    
                    # Execute the function
                    function_result = self.execute_function(function_name, function_args)
                    print(f"   Result: {function_result[:200]}...")
                    
                    # Add assistant's tool call to history (OpenRouter format)
                    self.conversation_history.append({
                        "role": "assistant",
                        "content": message.content,
                        "tool_calls": [
                            {
                                "id": tool_call_id,
                                "type": "function",
                                "function": {
                                    "name": function_name,
                                    "arguments": tool_call.function.arguments
                                }
                            }
                        ]
                    })
                    
                    # Add tool result to history (OpenRouter uses 'tool' role instead of 'function')
                    self.conversation_history.append({
                        "role": "tool",
                        "tool_call_id": tool_call_id,
                        "name": function_name,
                        "content": function_result
                    })
                
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
    print("Personal Assistant Agent (OpenRouter)")
    print("=" * 60)
    print("\nI can help you:")
    print("  📅 Book meetings (e.g., 'Book a meeting with John about project updates, his email is john@example.com')")
    print("  📧 Send emails (e.g., 'Send an email to sarah@example.com about the meeting tomorrow')")
    print("\nMake sure you've:")
    print("  1. Set up the n8n workflow (import personal_assistant_workflow.json)")
    print("  2. Configured Gmail and Google Calendar credentials in n8n")
    print("  3. Set N8N_WEBHOOK_URL in your .env file")
    print("  4. Set OPENROUTER_API_KEY in your .env file")
    print("  5. Optionally set OPENROUTER_MODEL (default: openai/gpt-4o-mini)")
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

