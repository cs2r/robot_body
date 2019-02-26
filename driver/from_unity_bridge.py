#!/usr/bin/env python
# -*- coding: UTF-8 -*-  # this is to add arabic coding to python
import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String

#file = open("/home/odroid/catkin_ws/src/robot_body/driver/robot_database.txt", "r")

dictionar = ['اب', 'اثنان', 'اجازة', 'اجتماع', 'اخ', 'اربعة', 'اسرة']
#dictionar.split()
print dictionar[0]
print dictionar[1]
print dictionar[3]
def callback(data):
	word = dictionar[data.data]
	word_pub.publish(word)

rospy.init_node('from_unity_bridge', anonymous=True)
word_pub = rospy.Publisher("/Word", String, queue_size=10)
rospy.Subscriber("/word_index", Int64, callback)

rospy.spin()
