# from IntentRecognizer.msg import Intent, POI_Object
import pyttsx


def generate_sentence(intent):
    #TODO
    #
    # ## intent object creation
    # intent = {'explain': False,
    #         'forward_distance': 2,
    #         'obstacle_label': 'chair',
    #         'obstacle_present': True,
    #         'poi_objects': [
    #                         {   'poi_depth': 2.775,
    #                             'poi_angle': 5.425,
    #                             'poi_deviation': True,
    #                             'poi_label': 'person'
    #                         }],
    #         'poi_present': True,
    #         'turn_direction': None
    #         }

    poi_count = len(intent["poi_objects"])
    poi_objects = intent["poi_objects"]

    obstacle_label = intent["obstacle_label"]
    obstacle_present = intent["obstacle_present"]

    explanation_sentence = ""

    if poi_count == 1:
        poi_object = intent["poi_objects"][0]
        poi_deviation = poi_object['poi_deviation'];
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





    #######################################################################
    # POI_counter =0
        # do nothing
    # poi_counter > 1
        # "I have there are n goals. "
        # starting from left to right, they are
            # 1. person
            # 2. person2
            # 3. person3
        # which one would you like to take me to?
    # poi_counter == 1
        # if there is poi_deviation
            # find poi angle and explain <right/lefe> "same as else but slightly <r/l>"
        # else
            #"I taking you to a <POI> in front of you."
        ## append explanation for obstable.
        # "and, I am daviating from the straight/desired path to avoid a <chair> on path."

    # Rule based sentences.

    # 1. Object related explanation
    # Object identification and it is at a certain distance at a certain angel.
    # obj_sentence = 'There is a ' + obj_name + ', ' + str(obj_distance) + ' meters away at ' + str(obj_angle) + ' degrees from you.'
    #
    # # 2. Goal related explanation
    # goal_sentence = 'I see a ' + goal_name + ' in the front.'
    #########################################################################

    return explanation_sentence

def speaker(sentence):
    engine = pyttsx.init()
    engine.say(sentence)
    engine.runAndWait()


def main():
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

    print(intent)
    sentence = generate_sentence(intent)

    print(sentence)

    # say the sentence in voice
    speaker(sentence)
    # engine.say(goal_sen)
    # engine.runAndWait()
    # engine.endLoop()


if __name__ == "__main__":
    main()
