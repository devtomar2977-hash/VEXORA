from modules.speech import listen
from modules.speak import speak
from modules.commands import process_command

print("===== VEXORA STARTED =====")

awake = False

while True:

    query = listen()

    if query is None:
        continue

    query = query.lower()

    print("You said:", query)

    # Wake VEXORA
    if not awake:

        if "hello" in query:

            awake = True
            speak("Hello Dev. I am Vexora. How can I help you today?")

        elif "exit" in query:

            speak("Goodbye Dev.")
            break

        else:

            print("Wake word not detected.")

    # Conversation Mode
    else:

        if "exit" in query:

            speak("Goodbye Dev.")
            break

        process_command(query)
