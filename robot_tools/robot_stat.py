#!/usr/bin/python
# -*- coding: UTF-8 -*-  # this is to add arabic coding to python
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import thread
from Tkinter import *
import rospy
from robot_body.msg import motorStat
from std_msgs.msg import Empty

empty_msg = Empty()
shutdown = rospy.Publisher('poppy/shutdown/', Empty, queue_size=1)
var = dict()
label = dict()
motorStatus = dict()
list = ['abs_z', 'bust_y', 'bust_x', 'head_z', 'head_y', 'l_shoulder_y', 'l_shoulder_x', 'l_arm_z', 'l_elbow_y',
            'l_forearm_z', 'r_shoulder_y', 'r_shoulder_x', 'r_arm_z', 'r_elbow_y', 'r_forearm_z']
ids = [33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55]
pos = [[3,3],[2,3],[2,4],[1,3],[0,3],[1,2],[1,1],[2,1],[3,1],[3,0],[1,5],[1,6],[2,6],[3,6],[3,7]]
infofont = ('times', 9, 'bold')
labelfont = ('times', 9)

def getMotorInfo(data):
    var[int(data.id)].set(str(data.name) + '\n' +
                          str(data.id) + '\n' +
                          str(data.present_load) + '\n' +
                          str(data.max_load) + '\n' +
                          str(data.present_voltage) + '\n' +
                          str(data.present_temperature))
    if (abs(data.present_load) in range(30,60)) | (data.present_temperature > 65):
        label[int(data.id)].config(fg='yellow')
    elif (abs(data.present_load) > 60) | (data.present_temperature in range(50,65)):
        label[int(data.id)].config(fg='red')
    elif data.present_voltage > 12.5:
        label[int(data.id)].config(fg='Blue')
    elif data.present_voltage < 11:
        label[int(data.id)].config(fg='cyan')
    else:
        label[int(data.id)].config(fg='green')
    if data.present_temperature in range(50,65):
        label[int(data.id)].config(bg='yellow')
    elif data.present_temperature > 65:
        label[int(data.id)].config(bg='red')
    else:
        label[int(data.id)].config(bg='white')


def robot_stat():
    rospy.init_node('robot_tools', anonymous=True)
    for name in list:
        rospy.Subscriber('poppy/get/' + name, motorStat, callback=getMotorInfo)
    print 'ROBOT_STATE subscribers successful Initial'
    rospy.spin()

def stop():
    print "stoping the robot"
    shutdown.publish(empty_msg)
    rospy.signal_shutdown('manual shutdown')

def main():
    master = Tk()
    master.geometry('510x420+0+0')
    master.title('ROBOT STATE')
    master.config(bg='white')
    info = Label(master, width=10,height=6,text='Name:\nId:\nLoad:\nMax_Load:\nVoltage:\nTemp:', font=infofont, bg='white')
    info.grid(row=0, column=2)
    image = PhotoImage(file='/home/odroid/catkin_ws/src/robot_body/robot_tools/stop.gif')
    Stop = Button(master, command=stop)
    Stop.config(image=image)
    Stop.image = image
    Stop.grid(row=0, column=5, columnspan=2)
    i=0
    for id in ids:
        var[id] = StringVar()
        label[id] = Label(master, width= 10, height= 6, textvariable=var[id], font=labelfont, bg='white')
        label[id].grid(row=pos[i][0], column=pos[i][1], columnspan=2 if id in [33, 36, 37] else 1)
        i+=1
    mainloop()

if __name__ == '__main__':
    thread.start_new_thread(main, ())
    robot_stat()


