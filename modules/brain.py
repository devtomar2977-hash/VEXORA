from modules.memory import remember, recall
from modules.commands import process_command
from modules.ai import ask_ai
from modules.speak import speak


def process_query(query):

    query = query.lower()

    # Remember user's name

    if "my name is" in query:

        name = query.replace("my name is", "").strip()

        remember("name", name)

        response = f"Okay {name}, I will remember your name."

        speak(response)

        return


# Recall user's name

    if "what is my name" in query:

        name = recall("name")

        if name:

            speak(f"Your name is {name}.")

        else:

            speak("I don't know your name yet.")

        return

    local_commands = [
        "google",
        "youtube",
        "linkedin",
        "calculator",
        "notepad",
        "vs code",
        "visual studio",
        "explorer",
        "time",
        "date",
    ]

    for command in local_commands:

        if command in query:

            process_command(query)
            return

    print("Thinking...")

    answer = ask_ai(query)

    print(answer)

    speak(answer)