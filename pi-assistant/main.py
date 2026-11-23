import threading
import time
import anthropic # Allows for ClaudeAPI
import os 
from dotenv import load_dotenv
from fastapi import FastAPI


# Loads .env file to be able to be called.
load_dotenv()
API_KEY = os.getenv("claude_api_key")
tools = [{
    "name": "set_alarm_tool",
    "description": "Allow Claude to set an alarm for you. Seconds are the main countdown. Minutes and hours will be converted into seconds. One minute is sixty seconds. One hour is sixty minutes. One hour is 3600 seconds.",
    "input_schema": {
    "type": "object",
    "properties": {
        "seconds": {
            "type": "integer",
            "description": "How much seconds are set for the alarm until it rings."
        }
    },
    "required": ["seconds"]
}
}]

def set_alarm(seconds):
    print(f"Alarm set for {seconds} seconds...")
    threading.Timer(seconds, play_sound).start()

        
def play_sound():
    print("\nTime's up!")
    os.system("afplay /System/Library/Sounds/Glass.aiff")

def claude_main():
    
    conversation = []
    
    while True:
        user_input = input("Prompt: ")
        if user_input.strip().lower() == "exit":
            break
        
        conversation.append({"role": "user", "content": user_input})
        
        client = anthropic.Anthropic(api_key=API_KEY)
        message = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=1024,
            messages=conversation,
            tools=tools
        )
        
      
      
      
      # Print command. Text content changes positions based on if the model begins to think or not. This catches the text at any position.
        for i in message.content:
            if i.type == "text":
                conversation.append({"role": "assistant", "content": i.text})
                print(i.text)
            elif i.type == "tool_use":
                if i.name == "set_alarm_tool":
                    set_alarm(i.input["seconds"])
                
            else:
             continue
        print(conversation)
    
if __name__ == "__main__":
    claude_main()