#!/usr/bin/env python

PKG = 'talker'
NAME = 'talker_test'

import unittest, rostest
import time
import rospy
from std_msgs.msg import *


class TestTalk(unittest.TestCase):

    def __init__(self, *args):
        super(TestTalk, self).__init__(*args)
        self.success = False

    def callback(self, data):
        print(rospy.get_caller_id(), "I heard %s"%data.data)
        self.success = data.data and data.data.startswith('hello_world')

    def test_talker(self):
        rospy.init_node(NAME, anonymous=True)
        rospy.Subscriber("/telemetry", String, self.callback)
        timeout_t = time.time() + 10.0 #10 seconds
        while not rospy.is_shutdown() and not self.success and time.time() < timeout_t:
            time.sleep(0.1)
        self.assertTrue(self.success)

if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestTalk, sys.argv)
