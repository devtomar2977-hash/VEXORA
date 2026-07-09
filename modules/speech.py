import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.8
recognizer.energy_threshold = 250
recognizer.dynamic_energy_threshold = True

def listen():

    with sr.Microphone() as source:

        print("🎤 Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("🎤 Listening...")

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        except sr.WaitTimeoutError:
            print("⌛ No speech detected.")
            return None

    try:

        print("🧠 Recognizing...")

        query = recognizer.recognize_google(audio, language="en-IN")

        return query

    except Exception:

        print("❌ Couldn't understand.")

        return None