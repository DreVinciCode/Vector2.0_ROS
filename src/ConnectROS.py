#!/usr/bin/env python3

import anki_vector
import rospy

from vector_ros.srv import BatteryState, BatteryStateResponse
from vector_ros.srv import SayText, SayTextResponse

from anki_vector.util import degrees, distance_mm, speed_mmps

from std_msgs.msg import Empty, Int16


class Vector_ROS(object):

    def __init__(self):

        try:
            rospy.init_node("vector_ros")

            # Vector_ROS(self.robot)
            
            self.vector_test_sub = rospy.Subscriber("/vector/drive", Empty, self.drive_callback)

            # with anki_vector.Robot(args.serial) as robot:
            #     print("Say 'Hello World'...")
            #     # robot.behavior.say_text("Sounds like a skills issue")
            #     robot.behavior.say_text("Hello World")


        except:
            print("Connection Failed")
        else:
            print("Connection Successful!")


        try:
            rospy.spin()
        except:
            rospy.logerr("Failed to call ROS spin")


    def drive_callback(self, data):
        print("Drive Called")
        robot.behavior.drive_straight(distance_mm(200), speed_mmps(50))
        

if __name__ == "__main__":
    Vector = Vector_ROS()
    args = anki_vector.util.parse_command_args()
            
    robot = anki_vector.Robot(args.serial)
    robot.connect()
