#! /usr/bin/env python

'''
Python Node for stopping the Robot when bumpers are pressed.

Author: Vinay (me@vnay.in)

'''

import sys
import rospy
from ros_arduino_msgs.srv import *
from ros_arduino_msgs.msg import *

def stop_robot():
    rospy.wait_for_service('arduino/stop_robot')
    try:
        stop_robot = rospy.ServiceProxy('arduino/stop_robot', StopRobot)
        stop_robot()
    except rospy.ServiceException, e:
        rospy.logerr('Service call failed:'+ e)



def process_bumper_bm_l1ff(data):
    if(data.value == 0):
    	rospy.loginfo(rospy.get_caller_id()+' Front Bumper Pressed.')
 	stop_robot()

def process_bumper_bm_l1fl(data):
    if(data.value == 0):
    	rospy.loginfo(rospy.get_caller_id()+' Front Left Bumper Pressed.')
 	stop_robot()

def process_bumper_bm_l1fr(data):
    if(data.value == 0):
    	rospy.loginfo(rospy.get_caller_id()+' Front Right Bumper Pressed.')
 	stop_robot()

def bumper_handle():
    #init ros node:
    rospy.init_node('bumper_handle', anonymous=True)

    rospy.Subscriber('arduino/sensor/bm_l1ff', Digital, process_bumper_bm_l1ff)
    rospy.Subscriber('arduino/sensor/bm_l1fl', Digital, process_bumper_bm_l1fl)
    rospy.Subscriber('arduino/sensor/bm_l1fr', Digital, process_bumper_bm_l1fr)
    
    rospy.loginfo(rospy.get_caller_id()+' started...')
    # Run the node
    rospy.spin()

if __name__ == "__main__":
    # Call bumper_handle function.
    bumper_handle()
