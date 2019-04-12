from pprint import pprint

import speech_recognition as sr
recognizer = sr.Recognizer()
STEP_SIZE = 2

def speech_to_text():
    with sr.Microphone() as sound_source:
        print("Say something")
        audio = recognizer.listen(sound_source)
        print("Audio recorded")
        return recognizer.recognize_google(audio).lower()

def identify_command():
    utterance = speech_to_text()

    print("'" + utterance + "'")
    if 'forward' in utterance:
        return {'forward_distance' : STEP_SIZE}
    elif 'stop' in utterance:
        return {'forward_distance': 0}
    elif 'left' in utterance:
        return {'turn_distance': 1.5708}
    elif 'right' in utterance:
        return {'turn_distance': -1.5708}
    elif 'goodboy' in utterance.replace(" ", ""):
        identify_command()
    else:
        return {'explain': 'Sorry, can you repeat?'}



def main():
    pprint(identify_command())


if __name__ == "__main__":
    main()