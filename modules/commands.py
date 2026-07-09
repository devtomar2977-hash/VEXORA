from modules.browser import open_google, open_youtube, open_linkedin
from modules.speak import speak
from modules.time_utils import get_time, get_date
from modules.system import (
    open_notepad,
    open_calculator,
    open_vscode,
    open_explorer
)
from modules.responses import random_opening

def process_command(command):

    print("process_command() received:", command)

    command = command.lower()

    if "google" in command:

        print("Opening Google...")
        speak(random_opening())
        open_google()

    elif "youtube" in command:

        print("Opening YouTube...")
        speak(random_opening())
        open_youtube()

    elif "linkedin" in command:

        print("Opening LinkedIn...")
        speak(random_opening())
        open_linkedin()

    elif "time" in command:

        speak(get_time())

    elif "date" in command:

        speak(get_date())
    elif "notepad" in command:

        speak(random_opening())
        open_notepad()

    elif "calculator" in command:

        speak(random_opening())
        open_calculator()

    elif "visual studio code" in command or "vs code" in command:

        speak(random_opening())
        open_vscode()

    elif "file explorer" in command or "explorer" in command:

        speak(random_opening())
        open_explorer()

    else:

        print("Unknown command")
        speak("Sorry Dev, I don't know that command.")  