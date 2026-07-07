import speech_recognition as sr

recognizer = sr.Recognizer()

recognizer.pause_threshold = 1

with sr.Microphone() as source:

    print("Listening.......")

    audio = recognizer.listen(source)

    print("Recognizing......")

    query = recognizer.recognize_google(audio)

    print(query)
