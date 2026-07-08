from modules.browser import open_google, open_youtube, open_linkedin
from modules.speak import speak

def process_command(command):

    print("process_command() received:", command)

    command = command.lower()

    if "google" in command:

        print("Opening Google...")
        speak("Opening Google")
        open_google()

    elif "youtube" in command:

        print("Opening YouTube...")
        speak("Opening YouTube")
        open_youtube()

    elif "linkedin" in command:

        print("Opening LinkedIn...")
        speak("Opening LinkedIn")
        open_linkedin()

    else:

        print("Unknown command")
        speak("Sorry Dev, I don't know that command.")