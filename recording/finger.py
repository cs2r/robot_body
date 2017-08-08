#!/usr/bin/python
import time
import tkFileDialog
import tkMessageBox
import tkSimpleDialog
from Tkinter import *
import rospy
from std_msgs.msg import Int16
from robot_body.msg import Emotion
import robot_tools.robot_tools as tools
import json
import numpy as np
import robot_tools.ssh_get_files as ssh_files



R = dict()
L = dict()

show=Emotion()
for servo in range(1, 10):
    R[servo] = rospy.Publisher('servo/R' + str(servo), Int16, queue_size=10)
    L[servo] = rospy.Publisher('servo/L' + str(servo), Int16, queue_size=10)
HEAD_EMO = rospy.Publisher('poppy/face/emotion', Emotion, queue_size=10)
HEAD_TXT = rospy.Publisher('poppy/face/text', Emotion, queue_size=10)


def __init__(master, movement, motor, pub):
    master.geometry('575x405')
    master.title('SETTING THE HAND')
    title = Frame(master)
    title.grid(row=0, column=0, columnspan=3, sticky=W+E+N+S)
    lefthand = LabelFrame(master, text="Left hand", bg = "red")
    lefthand.grid(row=1, column=0)
    righthand = LabelFrame(master, text="Right hand", bg = "green")
    righthand.grid(row=1, column=2)
    medButt = LabelFrame(master, text="Hands sets",bg = "blue")
    medButt.grid(row=1, column=1)
    buttfram = LabelFrame(master, text="Tools", bg="blue")
    buttfram.grid(row=2, column=0, columnspan=3, sticky=W+E+N+S)
    master.closing = False
    master.movement = movement
    active_motors = master.movement['actors_NAME']
    dead_motors = [name for name in motor if name not in active_motors]
    print('Starting the ROBOT')
    goal_position = {"Robot": [0 for name in dead_motors],
                     "Right_hand": [200, 200, 100, 100, 200, 100, 100, 100, 100],
                     "Left_hand": [200, 200, 100, 100, 200, 100, 100, 100, 100]}
    tools.go_to_pos(dead_motors, motor, goal_position, pub)

    goal_position = master.movement['position']['0']
    tools.go_to_pos(active_motors, motor, goal_position, pub)
    print('Robot started')



#//////////////////////////////////////////////////////////////////////////LEFT  ARM////////////////////////////////////////////////////////////////////////
    def LgetValue1(event):
        tools.left_servo_set(1, master.Lwrist_V.get(), L)

    master.Lwrist_V = Scale(lefthand, from_=100, to =300, orient = VERTICAL, length = 100, showvalue=0, command = LgetValue1)
    master.Lwrist_V.set(200)
    master.Lwrist_V.grid(row=2, column=0, rowspan=3, sticky=E)

    def LgetValue2(event):
        tools.left_servo_set(2, master.Lwrist_H.get(), L)

    master.Lwrist_H = Scale(lefthand, from_=100, to =300, orient = HORIZONTAL, length = 100, showvalue=0, command = LgetValue2)
    master.Lwrist_H.set(200)
    master.Lwrist_H.grid(row=4, column=1, columnspan=3, sticky=SW)

    def LgetValue3(event):
        tools.left_servo_set(3, master.Lthump_J.get(), L)

    master.Lthump_J = Scale(lefthand, from_=100, to =300, orient = HORIZONTAL, length = 75, showvalue=0, command = LgetValue3)
    master.Lthump_J.set(100)
    master.Lthump_J.grid(row=2, column=3, columnspan=2, sticky=NE)

    def LgetValue4(event):
        tools.left_servo_set(4, master.Lthump.get(), L)

    master.Lthump = Scale(lefthand, from_=100, to =300, orient = VERTICAL, length = 100, showvalue=0, command = LgetValue4)
    master.Lthump.set(100)
    master.Lthump.grid(row=0, column=4, rowspan=2, sticky=SE)

    def LgetValue5(event):
        tools.left_servo_set(5, master.LOpen.get(), L)

    master.LOpen = Scale(lefthand, from_=100, to =300, orient = HORIZONTAL, length = 125, showvalue=0, command = LgetValue5)
    master.LOpen.set(200)
    master.LOpen.grid(row=1, column=0, columnspan=4, sticky=W)

    def LgetValue6(event):
        tools.left_servo_set(6, master.Lindex.get(), L)

    master.Lindex = Scale(lefthand, from_=100, to =300, orient = VERTICAL, length = 100, showvalue=0, command = LgetValue6)
    master.Lindex.set(100)
    master.Lindex.grid(row=0, column=3)

    def LgetValue7(event):
        tools.left_servo_set(7, master.Lmajor.get(), L)

    master.Lmajor = Scale(lefthand, from_=100, to =300, orient = VERTICAL, length = 100, showvalue=0, command = LgetValue7)
    master.Lmajor.set(100)
    master.Lmajor.grid(row=0, column=2)

    def LgetValue8(event):
        tools.left_servo_set(8, master.Lring.get(), L)

    master.Lring = Scale(lefthand, from_=100, to =300, orient = VERTICAL, length = 100, showvalue=0, command = LgetValue8)
    master.Lring.set(100)
    master.Lring.grid(row=0, column=1)

    def LgetValue9(event):
        tools.left_servo_set(9, master.Lauri.get(), L)

    master.Lauri = Scale(lefthand, from_=100, to =300, orient = VERTICAL, length = 100, showvalue=0, command = LgetValue9)
    master.Lauri.set(100)
    master.Lauri.grid(row=0, column=0)
#//////////////////////////////////////////////////////////////////////////LEFT  ARM////////////////////////////////////////////////////////////////////////


#//////////////////////////////////////////////////////////////////////////RIGHT ARM////////////////////////////////////////////////////////////////////////
    def RgetValue1(event):
        tools.right_servo_set(1, master.Rwrist_V.get(), R)


    master.Rwrist_V = Scale(righthand, from_=100, to =300, orient=VERTICAL, length=100, showvalue=0, command=RgetValue1)
    master.Rwrist_V.set(200)
    master.Rwrist_V.grid(row=2, column=4, rowspan=3, sticky=W)


    def RgetValue2(event):
        tools.right_servo_set(2, master.Rwrist_H.get(), R)


    master.Rwrist_H = Scale(righthand, from_=100, to =300, orient=HORIZONTAL, length=100, showvalue=0, command=RgetValue2)
    master.Rwrist_H.set(200)
    master.Rwrist_H.grid(row=4, column=1, columnspan=3, sticky=SE)


    def RgetValue3(event):
        tools.right_servo_set(3, master.Rthump_J.get(), R)


    master.Rthump_J = Scale(righthand, from_=100, to =300, orient=HORIZONTAL, length=75, showvalue=0, command=RgetValue3)
    master.Rthump_J.set(100)
    master.Rthump_J.grid(row=2, column=0, columnspan=2, sticky=NW)


    def RgetValue4(event):
        tools.right_servo_set(4, master.Rthump.get(), R)


    master.Rthump = Scale(righthand, from_=100, to =300, orient=VERTICAL, length=100, showvalue=0, command=RgetValue4)
    master.Rthump.set(100)
    master.Rthump.grid(row=0, column=0, rowspan=2, sticky=SW)


    def RgetValue5(event):
        tools.right_servo_set(5, master.ROpen.get(), R)


    master.ROpen = Scale(righthand, from_=100, to =300, orient=HORIZONTAL, length=125, showvalue=0, command=RgetValue5)
    master.ROpen.set(200)
    master.ROpen.grid(row=1, column=1, columnspan=4, sticky=E)


    def RgetValue6(event):
        tools.right_servo_set(6, master.Rindex.get(), R)


    master.Rindex = Scale(righthand, from_=100, to =300, orient=VERTICAL, length=100, showvalue=0, command=RgetValue6)
    master.Rindex.set(100)
    master.Rindex.grid(row=0, column=1)


    def RgetValue7(event):
        tools.right_servo_set(7, master.Rmajor.get(), R)


    master.Rmajor = Scale(righthand, from_=100, to =300, orient=VERTICAL, length=100, showvalue=0, command=RgetValue7)
    master.Rmajor.set(100)
    master.Rmajor.grid(row=0, column=2)


    def RgetValue8(event):
        tools.right_servo_set(8, master.Rring.get(), R)


    master.Rring = Scale(righthand, from_=100, to =300, orient=VERTICAL, length=100, showvalue=0, command=RgetValue8)
    master.Rring.set(100)
    master.Rring.grid(row=0, column=3)


    def RgetValue9(event):
        tools.right_servo_set(9, master.Rauri.get(), R)


    master.Rauri = Scale(righthand, from_=100, to =300, orient=VERTICAL, length=100, showvalue=0, command=RgetValue9)
    master.Rauri.set(100)
    master.Rauri.grid(row=0, column=4)
#//////////////////////////////////////////////////////////////////////////RIGHT ARM////////////////////////////////////////////////////////////////////////


    def setframe(event):
        master.frm = master.recSlider.get()

        tools.do_seq(active_motors, 100, {'0':master.movement['position'][str(master.frm)]}, pub)

        if master.Lrec.get() == 0:
            tools.multi_servo_set(master.movement['position'][str(master.frm)]['Left_hand'], None, L)

        if master.Rrec.get() == 0:
            tools.multi_servo_set(None, master.movement['position'][str(master.frm)]['Right_hand'], None, R)


    def DelBefor():

        if tkMessageBox.askyesno(title='Warning', message='Warning: Do you want to delete the sequanses Befor the the frame ' + str(master.frm) + '?', parent=master):
            mov = {} #master.movement['position']

            newfrm=0
            for frm in range(master.frm, master.movement['frame_number'], 1):
                mov[str(newfrm)] = master.movement['position'][str(frm)]
                newfrm +=1
            master.movement.pop('position')
            master.movement['position'] = mov
            #master.movement['position'] = master.movement['position'][str(0):str(master.frm)]
            master.movement['frame_number']=newfrm
            master.recSlider.config(to=master.movement['frame_number'] - 1)
            master.recSlider.set(0)
            save.config(state=NORMAL)

    def DelAfter():

        if tkMessageBox.askyesno(title='Warning', message='Warning: Do you want to delete the sequanses After the the frame '+ str(master.frm) + '?', parent=master):
            for frm in range(master.frm, master.movement['frame_number'], 1):
                master.movement['position'].pop(str(frm))

            master.movement['frame_number'] = master.frm
            master.recSlider.config(to=master.movement['frame_number'] - 1)
            save.config(state=NORMAL)

    def closecall():
        if save['state']==NORMAL:
            decision = tkMessageBox.askyesnocancel('CLOSE', "Do you want to save sign: ", parent=master)
            if decision:
                savecall()
            elif decision is None:
                return
        print 'closing the robot'
        tools.multi_servo_set([200, 200, 100, 100, 200, 100, 100, 100, 100], [200, 200, 100, 100, 200, 100, 100, 100, 100], L, R)
        goal_position = {"Robot": [0 for name in dead_motors],
                         "Right_hand": [200, 200, 100, 100, 200, 100, 100, 100, 100],
                         "Left_hand": [200, 200, 100, 100, 200, 100, 100, 100, 100]}
        tools.go_to_pos(dead_motors, motor, goal_position, pub)
        goal_position = {"Robot": [0 for name in active_motors],
                         "Right_hand": [200, 200, 100, 100, 200, 100, 100, 100, 100],
                         "Left_hand": [200, 200, 100, 100, 200, 100, 100, 100, 100]}
        tools.go_to_pos(active_motors, motor, goal_position, pub)
        tools.releas(active_motors, pub)
        tools.multi_servo_set([0] * 9, [0] * 9, L, R)
        print 'Robot Closed'

        master.destroy()

    def savecall():
        print 'saving movement'
        saveFile = tkFileDialog.asksaveasfilename(defaultextension="json", initialdir="/home/odroid/catkin_ws/src/robot_body/recording/data_base", parent=master)
        if not saveFile:
            return None
        if list(master.emotion_list.curselection()):
            if master.emotion_list.get(master.emotion_list.curselection())=='show text':
                master.movement['text']=master.text.get()
            else:
                master.movement['emotion_name']=master.emotion_list.get(master.emotion_list.curselection())
            master.movement['emotion_time']=master.emotion_time.get()
        with open(saveFile, "w") as record:
            json.dump(master.movement, record)
        print 'saved'

    def setcall():
        print 'seting'
        master.lefthandpos = [master.Lwrist_V.get(), master.Lwrist_H.get(), master.Lthump_J.get(), master.Lthump.get(), master.LOpen.get(),
               master.Lindex.get(), master.Lmajor.get(), master.Lring.get(), master.Lauri.get()]
        master.righthandpos = [master.Rwrist_V.get(), master.Rwrist_H.get(), master.Rthump_J.get(), master.Rthump.get(), master.ROpen.get(),
                              master.Rindex.get(), master.Rmajor.get(), master.Rring.get(), master.Rauri.get()]
        master.movement['position'][str(master.frm)]['Left_hand'] = master.lefthandpos
        master.movement['position'][str(master.frm)]['Right_hand'] = master.righthandpos
        if master.frm not in master.setted_frame:
            master.setted_frame.append(master.frm)
            list(set(master.setted_frame))  # sort the list
        if ~master.needToBuild:
            master.needToBuild = True

        clear.config(state=NORMAL)
        print 'done'

    def find_smth_win():
        winSize = master.setted_frame[len(master.setted_frame)-1] - master.setted_frame[0]
        for i in range(len(master.setted_frame)-1):
            winSize = min(master.setted_frame[i+1]-master.setted_frame[i], winSize)
        return winSize;

    def buildPlay():
        if master.needToBuild:
            print 'building'
            #if master.setted_frame[0] != 0:
             #   master.setted_frame.insert(0, 0)
                #master.movement['position'][str(0)]['Left_hand'] = [200] * 9
                #master.movement['position'][str(0)]['Right_hand'] = [200] * 9
            if master.setted_frame[len(master.setted_frame) - 1] != master.movement['frame_number']:
                master.setted_frame.append(master.movement['frame_number'])
            index = 1
            while index < len(master.setted_frame):
                start = master.setted_frame[index - 1]
                stop = master.setted_frame[index]
                #        if (not master.movement['position'][str(0)]['Left_hand'])|(not master.movement['position'][str(0)]['Right_hand']):
                #            master.movement['position'][str(0)]['Left_hand'] = [200]*9
                #            master.movement['position'][str(0)]['Right_hand'] = [200]*9

                for frame in range(start + 1, stop, 1):
                    master.movement['position'][str(frame)]['Left_hand'] = master.movement['position'][str(start)]['Left_hand']
                    master.movement['position'][str(frame)]['Right_hand'] = master.movement['position'][str(start)]['Right_hand']
                index += 1
            print 'Done Building'

            print 'Smoothing the motion'

            win = find_smth_win()/int(2) if master.autoSmth.get() == 1 else master.smooth.get()
            for frame in range(master.movement['frame_number']):
                master.movement['position'][str(frame)]['Left_hand'] = np.mean([master.movement['position'][str(frame + i)]['Left_hand'] for i in range(min(master.movement['frame_number'] - frame-1, win)+1)], 0)
                master.movement['position'][str(frame)]['Right_hand'] = np.mean([master.movement['position'][str(frame + i)]['Right_hand'] for i in range(min(master.movement['frame_number'] - frame-1, win)+1)], 0)
                master.movement['position'][str(frame)]['Left_hand'] = list(np.int_(master.movement['position'][str(frame)]['Left_hand']))
                master.movement['position'][str(frame)]['Right_hand'] = list(np.int_(master.movement['position'][str(frame)]['Right_hand']))
            print 'Done Smoothing'
            master.needToBuild = False
            save.config(state=NORMAL)

        time.sleep(0.5)
        print 'Playing'
        goal_position = master.movement["position"]["0"]
        tools.go_to_pos(active_motors, motor, goal_position, pub, L, R)



        if list(master.emotion_list.curselection()):
            if master.emotion_list.get(master.emotion_list.curselection())=='show text':
                print 'text'
                HEAD_PUB = HEAD_TXT
                show.name = master.text.get()
            else:
                print 'emotion'
                HEAD_PUB = HEAD_EMO
                show.name = master.emotion_list.get(master.emotion_list.curselection())
            show.time = float(master.emotion_time.get())
            print show
        else:
            HEAD_PUB = None

        tools.do_seq(active_motors, master.movement["freq"], master.movement["position"],pub, L, R, HEAD_PUB, show)
        master.recSlider.set(master.movement["frame_number"])
        print 'Done'

    def clearcall():
        master.setted_frame = []
        master.needToBuild = False

    def setauto():
        master.smooth.config(state=NORMAL) if master.autoSmth.get() == 0 else master.smooth.config(state=DISABLED)

    def saveL():
        lefthandpos = [master.Lwrist_V.get(), master.Lwrist_H.get(), master.Lthump_J.get(), master.Lthump.get(),
                              master.LOpen.get(), master.Lindex.get(), master.Lmajor.get(), master.Lring.get(), master.Lauri.get()]
        name = tkSimpleDialog.askstring('Left Hand set name', 'Please enter the name of the Left hand set', parent=master)
        if name:
            handSetting["Left"][name] = lefthandpos
            L_handSets.insert(len(handSetting["Left"]), name)
        else:
            print "you Should enter the mane of the hand set"

        with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json", "w") as h:
            json.dump(handSetting, h)

    def saveR():
        righthandpos = [master.Rwrist_V.get(), master.Rwrist_H.get(), master.Rthump_J.get(), master.Rthump.get(),
                                master.ROpen.get(), master.Rindex.get(), master.Rmajor.get(), master.Rring.get(), master.Rauri.get()]
        name = tkSimpleDialog.askstring('Right Hand set name', 'Please enter the name of the Right hand set', parent=master)
        if name:
            handSetting["Right"][name] = righthandpos
            R_handSets.insert(len(handSetting["Right"]), name)
        else:
            print "you Should enter the mane of the hand set"

        with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json", "w") as h:
            json.dump(handSetting, h)

    def Lrel():
        tools.multi_servo_set([50] * 9, None, L)

    def Rrel():
        tools.multi_servo_set(None, [50] * 9, None, R)

    close = Button(buttfram, text='Close', width=5, command=closecall)
    close.grid(row=4, column=7, sticky=E)


    rel = Button(lefthand, text="Rel",width = 0, command =  Lrel)
    rel.grid(row=3, column=1)
    LSET = Button(lefthand, text=">>", width=0, command=saveL)
    LSET.grid(row=3, column=3)
    master.Lrec = IntVar(lefthand,value=0)
    recL = Checkbutton(lefthand, variable=master.Lrec)
    recL.grid(row=3, column=2)

    rer = Button(righthand, text="Rel", width=0, command= Rrel)
    rer.grid(row=3, column=3)
    RSET = Button(righthand, text="<<", width=0, command=saveR)
    RSET.grid(row=3, column=1)
    master.Rrec = IntVar(righthand, value=0)
    recR = Checkbutton(righthand, variable=master.Rrec)
    recR.grid(row=3, column=2)


    L_handSets = Listbox(medButt, height=10, width=10)
    L_handSets.grid(row=2, column=0, columnspan=2)
    R_handSets = Listbox(medButt, height=10, width=10)
    R_handSets.grid(row=2, column=2, columnspan=2)
    try:
        with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json", "r") as f:
            handSetting = json.load(f)

        for name, pos in handSetting["Left"].items():

            L_handSets.insert(END, (name))
        for name, pos in handSetting["Right"].items():

            R_handSets.insert(END, (name))
    except Exception, err:
        print err


    def setleft():
        if list(L_handSets.curselection()):
            left_values = handSetting["Left"][L_handSets.get(L_handSets.curselection())]
            tools.multi_servo_set(left_values, None, L)
            master.Lwrist_V.set(left_values[0])
            master.Lwrist_H.set(left_values[1])
            master.Lthump_J.set(left_values[2])
            master.Lthump.set(left_values[3])
            master.LOpen.set(left_values[4])
            master.Lindex.set(left_values[5])
            master.Lmajor.set(left_values[6])
            master.Lring.set(left_values[7])
            master.Lauri.set(left_values[8])
        else:
            print "No setting is selected"

    def setright():
        if list(R_handSets.curselection()):
            right_values = handSetting["Right"][R_handSets.get(R_handSets.curselection())]
            tools.multi_servo_set(None, right_values, None, R)
            master.Rwrist_V.set(right_values[0])
            master.Rwrist_H.set(right_values[1])
            master.Rthump_J.set(right_values[2])
            master.Rthump.set(right_values[3])
            master.ROpen.set(right_values[4])
            master.Rindex.set(right_values[5])
            master.Rmajor.set(right_values[6])
            master.Rring.set(right_values[7])
            master.Rauri.set(right_values[8])
        else:
            print "No setting is selected"


    def L_DEL():

        if list(L_handSets.curselection()):
            if tkMessageBox.askyesno(title='Warning', message='do you want to DELETE ' + L_handSets.get(L_handSets.curselection()) + ' ?', parent=master):
                with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json") as f:
                    handSetting = json.load(f)
                del handSetting["Left"][L_handSets.get(L_handSets.curselection())]
                L_handSets.delete(L_handSets.curselection())
                with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json", "w") as f:
                    json.dump(handSetting, f)
        else:
            print "No setting is selected"

    def R_DEL():

        if list(R_handSets.curselection()):
            if tkMessageBox.askyesno(title='Warning', message='do you want to DELETE ' + R_handSets.get(R_handSets.curselection()) + ' ?', parent=master):
                with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json", "r") as f:
                    handSetting = json.load(f)
                del handSetting["Right"][R_handSets.get(R_handSets.curselection())]
                R_handSets.delete(R_handSets.curselection())
                with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json", "w") as f:
                    json.dump(handSetting, f)
        else:
            print "No setting is selected"

    leftSet = Button(medButt, text="<<", width=0, command=setleft)
    leftSet.grid(row=3, column=0, sticky=E)
    LDEL = Button(medButt, text="DEL", width=0, command=L_DEL)
    LDEL.grid(row=3, column=1, sticky=W)

    rightSet = Button(medButt, text=">>", width=0, command=setright)
    rightSet.grid(row=3, column=3, sticky=W)
    RDEL = Button(medButt, text="DEL", width=0, command=R_DEL)
    RDEL.grid(row=3, column=2, sticky=E)
    master.steps = StringVar(master, value=1)
    master.frm = 0
    master.recSlider = Scale(buttfram, from_=0, to=master.movement['frame_number']-1, orient=HORIZONTAL, length=430, showvalue=0, command=setframe)
    master.recSlider.set(0)
    master.recSlider.grid(row=0, column=1, columnspan=6)
    del_befor = Button(buttfram, text='Del', width=5, command=DelBefor)
    del_befor.grid(row=0, column=0)
    del_after = Button(buttfram, text='Del', width=5, command=DelAfter)
    del_after.grid(row=0, column=7)
    master.autoSmth = IntVar(master, value=1)
    master.autoSmooth = Checkbutton(buttfram, text='Auto', variable=master.autoSmth, command=setauto)
    master.autoSmooth.grid(row=1, column=1)
    master.smooth = Scale(buttfram, from_=0, to=master.movement['frame_number']-1, orient=HORIZONTAL, length=100, showvalue=0)
    master.smooth.set(min(30, master.movement['frame_number'] - 1))
    master.smooth.grid(row=1, column=2, sticky=W)
    master.smooth.config(state=DISABLED)
    setpos = Button(buttfram, text='Set', width=5, command=setcall)
    setpos.grid(row=1, column=0)
    build = Button(buttfram, text='Build', width=5, command=buildPlay)
    build.grid(row=2, column=0)
    save = Button(buttfram, text='Save', width=5, command=savecall)
    save.grid(row=3, column=0)
    save.config(state=DISABLED)
    clear = Button(buttfram, text='Clear', width=5, command=clearcall)
    clear.grid(row=4, column=0)
    clear.config(state=DISABLED)
    master.text_to_show = Label(buttfram, text="Text to show:")
    master.text_to_show.grid(row=1,  column=3, sticky=E)
    master.text = StringVar()
    master.textEntry = Entry(buttfram, width=10, textvariable=master.text)
    master.textEntry.grid(row=1, column=4, sticky=W)

    master.emotion_to_show = Label(buttfram, text="Emotion to show:")
    master.emotion_to_show.grid(row=2,  column=3, sticky=E)
    master.emotion_list = Listbox(buttfram, width=10, height=5)
    master.emotion_list.grid(row=2, column=4, rowspan=3, sticky=W)

    emotions = ssh_files.get("head", "pi", "headdriver", "/home/pi/catkin_ws/src/head_driver_pkg/src/emotions", '"*.gif"')
    emotions.insert(0,"show text")
    for name in emotions:
        master.emotion_list.insert(END, str(name))

    master.showing_time = Label(buttfram, text="Time:")
    master.showing_time.grid(row=1, column=5, sticky=E)
    master.emotion_time = StringVar(value=2)
    master.emotion_timeEntry = Entry(buttfram, width=3, textvariable=master.emotion_time)
    master.emotion_timeEntry.grid(row=1, column=6, sticky=W)
    master.needToBuild = False
    master.setted_frame = []
