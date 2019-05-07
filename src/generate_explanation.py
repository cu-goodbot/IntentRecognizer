import pyttsx

def generate_sentence(intent):
    '''
    Function to form natural language sentences from 'intent'
    :param intent: Intent dict object from 'intent_wrapper.py'
    :return: sentence in string form
    '''
    poi_count = len(intent["poi_objects"])
    poi_objects = intent["poi_objects"]

    obstacle_label = intent["obstacle_label"]
    obstacle_present = intent["obstacle_present"]

    explanation_sentence = ""

    if poi_count == 1:
        poi_object = intent["poi_objects"][0]
        poi_deviation = poi_object['poi_deviation']
        if poi_deviation > 0:
            poi_angle = poi_object['poi_angle']
            poi_label = poi_object['poi_label']
            if poi_angle > 0:
                explanation_sentence = "I am taking you to a " + poi_label + " in front of you which is slightly towards right."
            else:
                explanation_sentence = "I am taking you to a " + poi_label + " in front of you which is slightly towards left."
        if obstacle_present == True:
            explanation_sentence = explanation_sentence + " and I am deviating from the straight path to avoid a " + obstacle_label + " in path."
    if poi_count > 1:
        explanation_sentence = "I see there are " + str(poi_count) + " goals. starting from left to right, they are,"
        pois = ""
        num = 0
        for obj in poi_objects:
            poi_label = obj['poi_label']
            if num != 0:
                pois = pois + " and " + poi_label
            else:
                pois = pois + " " + poi_label
            num += 1
        explanation_sentence = explanation_sentence + pois + ", which one would you like me to take you to?"

    return explanation_sentence

def speaker(sentence):
    '''
    Function to generate speech from text
    :param sentence: Text
    :return: None
    '''
    engine = pyttsx.init()
    engine.say(sentence)
    engine.runAndWait()


def main():
    '''
    A local function to just test the code
    :return: None
    '''
    intent = {'explain': False,
              'forward_distance': 2,
              'obstacle_label': 'chair',
              'obstacle_present': True,
              'poi_objects': [
                  {'poi_depth': 2.775,
                   'poi_angle': 5.425,
                   'poi_deviation': True,
                   'poi_label': 'person'
                   },
                  {'poi_depth': 2.775,
                   'poi_angle': 5.425,
                   'poi_deviation': True,
                   'poi_label': 'door'
                   }
              ],
              'poi_present': True,
              'turn_direction': None
              }

    sentence = generate_sentence(intent)
    print(sentence)

    # say the sentence
    speaker(sentence)


if __name__ == "__main__":
    main()
