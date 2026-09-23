import os
import logging

from dotenv import load_dotenv
from langchain_groq import ChatGroq

logging.disable(logging.WARNING)

# Load environment variables
load_dotenv()

api_key = os.environ["GROQ_API_KEY"]

print("1. Key loaded")
print("2. Creating model...")

llm = ChatGroq(
    model="qwen/qwen3.8-27b",
    groq_api_key=api_key,
    reasoning_format="parsed"
)

print("3. Calling model...")

message = llm.invoke([
    {
        "role": "system",
        "content": "You are a helpful assistant that answers in one short line."
    },
    {
        "role": "human",
        "content": "How many planets are in the solar system?"
    }
])

print("4. Response received")
print(message.content)