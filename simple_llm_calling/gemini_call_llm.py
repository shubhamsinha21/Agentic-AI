import os
import logging

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

logging.disable(logging.WARNING)

# Load environment variables
load_dotenv()

api_key = os.environ["GOOGLE_API_KEY"]

print("1. Key loaded")
print("2. Creating model...")

llm = ChatGoogleGenerativeAI(
    model="gemma-4-31b-it",
    google_api_key=api_key,
)

print("3. Calling model...")

response = llm.invoke([
    ["system", "You are a helpful assistant that answers in one short line."],
    ["human", "how many moons does jupiter have?"]
])

print("4. Response received")
print(response.text)

prompt = "Write a single tagline for a quirky cofee shop. Only output the tagline, nothing else."
llm2 = ChatGoogleGenerativeAI(model="gemma-4-31b-it", temperature=1)
response2 = llm2.invoke(prompt)
print(response2.text)