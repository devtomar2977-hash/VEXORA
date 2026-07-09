import random

OPENING_RESPONSES = [
    "Right away.",
    "Certainly.",
    "Working on it.",
    "Done.",
    "Opening it now.",
]

def random_opening():
    return random.choice(OPENING_RESPONSES)