import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

recognizer.pause_threshold = 0.8
recognizer.energy_threshold = 250
recognizer.dynamic_energy_threshold = True


def setup_microphone():
    with microphone as source:
        print("🎤 Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)


def listen():

    with microphone as source:

        print("🎤 Listening...")

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

        except sr.WaitTimeoutError:

            print("⌛ No speech detected.")
            return None

    try:

        print("🧠 Recognizing...")

        query = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        return query

    except sr.UnknownValueError:

        print("❌ Couldn't understand.")
        return None

    except sr.RequestError:

        print("🌐 Google Speech Service unavailable.")
        return None