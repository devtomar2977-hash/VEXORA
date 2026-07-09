from datetime import datetime

def log_command(command):

    with open("logs/assistant.log", "a") as file:

        time = datetime.now().strftime("%H:%M:%S")

        file.write(f"[{time}] {command}\n")