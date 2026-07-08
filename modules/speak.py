import asyncio
import edge_tts
from playsound import playsound
import os

VOICE = "en-US-GuyNeural"

async def generate_voice(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("voice.mp3")

def speak(text):

    asyncio.run(generate_voice(text))

    playsound("voice.mp3")

    if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")