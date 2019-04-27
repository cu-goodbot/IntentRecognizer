#!/usr/bin/env python

"""
ROS wrapper for Intent Recognition module.
"""
from pprint import pprint

import rospy
import json
from std_msgs.msg import String
from intent_recognizer.msg import Scene, Intent, POI_Object

from speech_to_text import speech_to_text, identify_command, indentify_poi
from generate_explanation import generate_sentence, speaker

POI_ANGLE_THRESHOLD = 3
OBSTACLE_ANGLE_THRESHOLD = 30

class IntentWrapper(object):

    def __init__(self):

        # last recorded user input statement in text
        self.utterance = None
        # flag for if input has been received
        self.input_flag = False
        # Latest POI info
        self.POI_info = None

        # create publishers and subscribers
        intent_pub = rospy.Publisher('/intent',Intent,queue_size=10)
        rospy.Subscriber('/scene_info', Scene, self.get_POI_info)

        rospy.init_node('intent_recognizer')

        rate = rospy.Rate(20)

        while not rospy.is_shutdown():

            # wait for user to hit button and begin speaking
            intent = self.get_input()

            # Check if the user asks for an explanation
            if intent["explain"]:
                # TODO pause Movo mometarily
                sentence = generate_sentence(intent)
                speaker(sentence)
            
            # create intent message
            # flat_data = json.dumps(data)

            # Block the intent publication until POI is disambiguated
            # TODO

            # publish message
            msg = Intent(**intent)
            intent_pub.publish(msg)

            rate.sleep()


    def get_POI_info(self, msg):
        """
        Scene info callback. Gets POI info from scene_info to infer true intent
        :return: TODO
        """
        self.POI_info = msg

    
    def get_input(self):
        """
        Wait for user input, beginning w/ button press, and turn speech into intnet.
        """
        # wait for button press
        raw_input('Press r and then enter and then speak input\n')
        intent = identify_command()
        intent["poi_objects"] = []
        intent["poi_present"] = False
        intent["obstacle_present"] = False
        intent["obstacle_label"] = None

        # Add POI info to generate the true intent
        for obstacle in self.POI_info.objects:
            if obstacle.label == 'person':
                base_poi_object = {"poi_depth" : obstacle.depth,
                                   "poi_angle" : obstacle.angle,
                                   "poi_deviation" : abs(obstacle.angle) > POI_ANGLE_THRESHOLD,
                                   "poi_label" : obstacle.label}
                intent["poi_present"] = True
                poi_object = POI_Object(**base_poi_object)
                intent["poi_objects"].append(poi_object)
            elif abs(obstacle.angle) < OBSTACLE_ANGLE_THRESHOLD and not intent["obstacle_present"]:
                intent["obstacle_present"] = True
                intent["obstacle_label"] = obstacle.label

        return intent

if __name__ == "__main__":
    IntentWrapper()