import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

try:
    response = model.generate_content("Say hello in one short sentence.")
    print(response.text)

except Exception as e:
    print(e)