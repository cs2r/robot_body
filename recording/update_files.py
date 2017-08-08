#!/usr/bin/python
import os
import json

path = "/home/odroid/catkin_ws/src/robot_body/recording/data_base/"
dir = os.listdir(path)
for file in dir:
    if file[-5:]==".json":
        if raw_input ("Do you want to change this file: " + file + " y/n: ") == "y":
            with open(path+file, 'r') as sign:
                movement = json.load(sign)
                movement["emotion_name"]=''
                movement["text"] = ''
                movement["emotion_time"] = []
            with open(path+file, 'w') as sign:
                json.dump(movement,sign)
print "done"
