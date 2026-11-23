import anthropic
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("claude_api_key")
client = anthropic.Anthropic(api_key=API_KEY)
message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, world"}],
)
print(message.content[0].text)