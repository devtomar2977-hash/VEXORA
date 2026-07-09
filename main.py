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

    from modules.logger import log_command

    log_command(query)

    if not awake:

        if "hello" in query:

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

            speak("Goodbye Dev.")

            break

        else:

            from modules.brain import process_query

            process_query(query)

<<<<<<< HEAD
        from modules.brain import process_query

        process_query(query)
=======
        else:

            process_command(query)
>>>>>>> main
