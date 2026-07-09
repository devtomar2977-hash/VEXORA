import asyncio
import edge_tts
import pygame
import os
import time
from config import VOICE

pygame.mixer.init()

async def generate_voice(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("voice.mp3")

def speak(text):

    asyncio.run(generate_voice(text))

    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()

    os.remove("voice.mp3")