from pprint import pprint
# from SceneUnderstanding.src.object_detection import obstacle_detector
import speech_recognition as sr
recognizer = sr.Recognizer()
STEP_SIZE = 2

def speech_to_text():
    with sr.Microphone() as sound_source:
        print("Say something")
        audio = recognizer.listen(sound_source)
        print("Audio recorded")
        try:
            return recognizer.recognize_google(audio).lower()
        except:
            return "forward"


def identify_command():
    utterance = speech_to_text()

    print("'" + utterance + "'")
    if 'forward' in utterance:
        return {'forward_distance' : STEP_SIZE,
                'turn_direction': None}
    elif 'stop' in utterance:
        return {'forward_distance': 0,
                'turn_direction': None}
    elif 'left' in utterance:
        return {'turn_direction': 'left',
                'forward_distance' : STEP_SIZE}
    elif 'right' in utterance:
        return {'turn_direction': 'right',
                'forward_distance' : STEP_SIZE,}
    else:
        return {'explain': 'Sorry, can you repeat?'}


def main():
    pprint(identify_command())


if __name__ == "__main__":
    main()
    # print(obstacle_detector)