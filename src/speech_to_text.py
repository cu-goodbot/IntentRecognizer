from pprint import pprint
# from SceneUnderstanding.src.object_detection import obstacle_detector
import speech_recognition as sr
recognizer = sr.Recognizer()
STEP_SIZE = 2

def speech_to_text(ask_poi = False):

    # set threshold for input
    with sr.Microphone() as sound_source:
        recognizer.adjust_for_ambient_noise(sound_source)
    print('Set input energy threshold to: {}'.format(recognizer.energy_threshold))

    with sr.Microphone() as sound_source:
        print("Say something")
        audio = recognizer.listen(sound_source)
        print("Audio recorded")
        try:
            return recognizer.recognize_sphinx(audio).lower()
        except:
            if ask_poi:
                return "POI not clear"
            return "forward"

def form_intent(step_size = STEP_SIZE, direction = None, explain = False):
    return {
        'turn_direction': direction,
        'forward_distance': step_size,
        'explain': explain
    }


def identify_command():
    utterance = speech_to_text()

    print("'" + utterance + "'")
    if 'forward' in utterance:
        return form_intent()
    elif 'stop' in utterance:
        return form_intent(step_size=0)
    elif 'left' in utterance:
        return form_intent(direction='left')
    elif 'right' in utterance:
        return form_intent(direction='right')
    elif len(set(utterance.split()).intersection({'explain', 'what', 'why'})) > 0:
        return form_intent(explain=True)
    else:
        return {'explain': 'Sorry, can you repeat?'}

def identify_poi():
    utterance = speech_to_text(ask_poi=True)
    if 'first' in utterance:
        return 0
    elif 'second' in utterance:
        return 1
    elif 'third' in utterance:
        return 2
    else:
        # If the utterance was not inferred or delivered
        # correctly the left most POI is selected
        return 0

def main():
    pprint(identify_command())


if __name__ == "__main__":
    main()
    # print(obstacle_detector)
