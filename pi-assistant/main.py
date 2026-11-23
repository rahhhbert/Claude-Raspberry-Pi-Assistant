import anthropic # Allows for ClaudeAPI
import os 
from dotenv import load_dotenv
from fastapi import FastAPI


# Loads .env file to be able to be called.
load_dotenv()


# API_KEY = os.getenv("claude_api_key")
# client = anthropic.Anthropic(api_key=API_KEY)
# message = client.messages.create(
#     model="claude-haiku-5-5",
#     max_tokens=1024,
#     messages=[{"role": "user", "content": "Hello, world"}],
# )
# print(message.content[0].text)


def claude_main():
    
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break
        print(f"You typed: {user_input}")    
    
if __name__ == "__main__":
    claude_main()