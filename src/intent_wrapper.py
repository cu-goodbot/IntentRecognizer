#!/usr/bin/env python

"""
ROS wrapper for Intent Recognition module.
"""

import rospy
import json
from std_msgs.msg import String
from rospy_message_converter import message_converter

from speech_to_text import speech_to_text, identify_command

class IntentWrapper(object):

    def __init__(self):

        # last recorded user input statement in text
        self.utterance = None
        # flag for if input has been received
        self.input_flag = False

        # create publishers and subscribers
        intent_pub = rospy.Publisher('intent',String,queue_size=10)

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

    
    def get_input(self):
        """
        Wait for user input, beginning w/ button press, and turn speech into intnet.
        """
        # wait for button press
        raw_input('Press r and then enter and then speak input')
        utterance = identify_command()
        # utterance = {'turn_distance': 1.5708}

        return utterance

if __name__ == "__main__":
    IntentWrapper()