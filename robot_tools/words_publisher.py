#!/usr/bin/python
# -*- coding: UTF-8 -*-  # this is to add arabic coding to python
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from Tkinter import *
import time
import rospy
from std_msgs.msg import String
pub = rospy.Publisher('Word', String, queue_size=10)


def send_word_s():
    words = text.get()
    words_list = words.split()
    for word in words_list:
        pub.publish(word)
        time.sleep(0.2)

rospy.init_node('WORD_PUBLISHER', anonymous=True)
master = Tk()
master.geometry('240x50')
master.title('SEND WORDS')
text = StringVar()
Input = Entry(master, width=20, textvariable=text)
Input.grid(row=0, column=0)
publish=Button(master, text='send', command=send_word_s)
publish.grid(row=1, column=0)
mainloop()
