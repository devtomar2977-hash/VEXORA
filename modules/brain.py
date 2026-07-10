from modules.commands import process_command
from modules.ai import ask_ai
from modules.speak import speak


def process_query(query):

    query = query.lower()

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