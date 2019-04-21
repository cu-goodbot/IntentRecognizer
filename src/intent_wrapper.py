#!/usr/bin/env python

"""
ROS wrapper for Intent Recognition module.
"""

import rospy
import json
from std_msgs.msg import String
# from rospy_message_converter import message_converter
from scene_understanding.msg import Scene

from speech_to_text import speech_to_text, identify_command

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
        intent_pub = rospy.Publisher('intent',String,queue_size=10)
        rospy.Subscriber('/scene_info', Scene, self.get_POI_info)

        rospy.init_node('intent_recognizer')

        rate = rospy.Rate(20)

        while not rospy.is_shutdown():

            # wait for user to hit button and begin speaking
            data = self.get_input()
            
            # create intent message
            flat_data = json.dumps(data)

            # publish message
            msg = String()
            msg.data = flat_data
            intent_pub.publish(msg)


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
        intent["poi_present"] = False
        intent["poi_depth"] = None
        intent["poi_angle"] = None
        intent["poi_deviation"] = False
        intent["obstacle_present"] = False
        intent["obstacle_label"] = None

        # Add POI info to generate the true intent
        for obstacle in self.POI_info.objects:
            if obstacle.label == 'person':
                intent["poi_present"] = True
                intent["poi_depth"] = obstacle.depth
                intent["poi_angle"] = obstacle.angle
                if abs(obstacle.angle) > POI_ANGLE_THRESHOLD:
                    intent["poi_deviation"] = True
            elif abs(obstacle.angle) < OBSTACLE_ANGLE_THRESHOLD and not intent["obstacle_present"]:
                intent["obstacle_present"] = True
                intent["obstacle_label"] = obstacle.label

        return intent

if __name__ == "__main__":
    IntentWrapper()