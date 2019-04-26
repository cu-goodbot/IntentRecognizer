import pyttsx


def generate_sentence(obj_name, obj_distance, obj_angle, goal_distance, goal_angle, goal_name):

    # Rule based sentences.

    # 1. Object related explanation
    # Object identification and it is at a certain distance at a certain angel.
    obj_sentence = 'there is a ' + obj_name + ', ' + str(obj_distance) + ' meters away at ' + str(obj_angle) + ' degrees from you.'

    # 2. Goal related explanation
    goal_sentence = 'I see a ' + goal_name + ' in the front.'

    return obj_sentence, goal_sentence


def main():

    obj_sen, goal_sen = generate_sentence('chair', 2.0, 5, 5, 10, 'door')

    print(obj_sen)
    print(goal_sen)

    # say the sentence in voice
    engine = pyttsx.init()
    engine.say(obj_sen)
    # engine.runAndWait()
    engine.say(goal_sen)
    engine.runAndWait()
    engine.endLoop()



if __name__ == "__main__":
    main()
