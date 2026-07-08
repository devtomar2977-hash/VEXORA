from modules.speech import listen
from modules.speak import speak
from modules.browser import open_google, open_youtube
import time

print("===== VEXORA STARTED =====")

while True:

    query = listen()

    if query is None:
        continue

    print("You said:", query)

    if "hello" in query:

        speak("Hello Dev. I am vexora, How can I help you today?")

        command = listen()

        if command is None:
            continue

        command = command.lower()

        print(repr(command))

        if "google" in command:

            speak("Opening Google")
            time.sleep(1)
            open_google()
            speak("Google has been opened.")

        elif "youtube" in command:

            speak("Opening YouTube")
            time.sleep(1)
            open_youtube()
            speak("youtube is ready.")

        elif "exit" in command:

            speak("Goodbye Dev. Have a nice day")

            break

        else:

            speak("Sorry Dev. I don't know that command.")

    elif "exit" in query:

        speak("Goodbye Dev.")

        break
