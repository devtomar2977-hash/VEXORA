from modules.speech import listen, setup_microphone
from modules.speak import speak
from modules.logger import log_command
from modules.brain import process_query

print("===== VEXORA STARTED =====")

setup_microphone()

awake = False

while True:

    query = listen()

    if query is None:
        continue

    query = query.lower()

    print("You said:", query)

    log_command(query)

    if not awake:

        if query.startswith("hello"):

            awake = True
            speak("Hello Dev. I am Vexora. How can I help you today?")

        elif "exit" in query:

            speak("Goodbye Dev.")
            break

        else:

            print("Wake word not detected.")

    else:

        if "sleep" in query:

            speak("Going to sleep. Say Hello when you need me.")
            awake = False

        elif "exit" in query:
            print("DEBUG: Sleep command detected")
            speak("Goodbye Dev.")
            break

        else:

            process_query(query)    