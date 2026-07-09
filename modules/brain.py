from modules.commands import process_command
from modules.ai import ask_ai


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

    # Anything else goes to AI
    ask_ai(query)