from modules.commands import process_command


def process_query(query):

    query = query.lower()

    # Commands handled locally
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
        "date"
    ]

    for command in local_commands:

        if command in query:

            process_command(query)

            return

    # Everything else goes to AI

    print("Routing to AI...")