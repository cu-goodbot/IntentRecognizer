import pyttsx


def generate_sentence(intent):
    #TODO

    POI_counter = len(intent["poi_objects"])

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

    return "work in progress"

def speaker(sentence):
    engine = pyttsx.init()
    engine.say(sentence)
    engine.runAndWait()


def main():

    obj_sen, goal_sen = generate_sentence('chair', 2.0, 5, 5, 10, 'door')

    print(obj_sen)
    print(goal_sen)

    # say the sentence in voice
    engine = pyttsx.init()
    engine.say(obj_sen)
    engine.runAndWait()
    # engine.say(goal_sen)
    # engine.runAndWait()
    # engine.endLoop()


if __name__ == "__main__":
    main()
