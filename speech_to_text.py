import speech_recognition as sr

# Some unorganised trial code

recognizer = sr.Recognizer()

with sr.Microphone() as sound_source:
    print("Say something")
    audio = recognizer.listen(sound_source)
    print("Audio recorded")

print(recognizer.recognize_google(audio))