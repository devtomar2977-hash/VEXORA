import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

key = os.getenv("GEMINI_API_KEY")
print("API Key loaded:", key[:10] + "..." if key else "No key found")

genai.configure(api_key=key)

print("\nAvailable models:\n")

for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(model.name)