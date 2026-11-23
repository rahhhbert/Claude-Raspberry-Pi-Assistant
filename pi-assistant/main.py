import anthropic # Allows for ClaudeAPI
import os 
from dotenv import load_dotenv
from fastapi import FastAPI


# Loads .env file to be able to be called.
load_dotenv()
API_KEY = os.getenv("claude_api_key")



def claude_main():
    
    conversation = []
    
    while True:
        user_input = input("Prompt: ")
        if user_input.strip().lower() == "exit":
            break
        
        
        client = anthropic.Anthropic(api_key=API_KEY)
        message = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": user_input}],
        )
        conversation.append([{"role": "user", "content": user_input}])
      
      
      
      # Print command. Text content changes positions based on if the model begins to think or not. This catches the text at any position.
        for i in message.content:
            if i.type == "text":
                conversation.append([{"role": "assistant", "content": i.text}])
                print(i.text)
            else:
             continue
        print(conversation)
    
if __name__ == "__main__":
    claude_main()