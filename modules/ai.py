import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Updated model
model = genai.GenerativeModel("gemini-flash-latest")

def ask_ai(question):
    try:
        response = model.generate_content(question)
        return response.text
    
    except Exception as e:

        error = str(e)  

        if "429" in error:
            return "I'm receiving too many requests right now. Please wait one minute and try again."

        return f"Sorry Dev. AI Error: {error}"
    