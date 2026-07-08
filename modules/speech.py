import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

            print("🧠 Recognizing...")

            query = recognizer.recognize_google(audio)

            return query.lower()

        except sr.UnknownValueError:
            print("❌ Couldn't understand.")
            return None

        except sr.WaitTimeoutError:
            print("⌛ No speech detected.")
            return None

        except Exception as e:
            print("Error:", e)
            return None


