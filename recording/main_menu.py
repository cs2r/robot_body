from Tkinter import *
import tkFileDialog
import tkMessageBox
from pypot.robot import config
import thread
import json
import time




class MAIN():

    def Close_call(self):
        self.master.destroy()

    def action(self, parent):
        for name in config.robot_2_config["motorgroups"][parent]:
            if self.check_button_value[parent].get():
                self.check_button[name].select()
            else:
                self.check_button[name].deselect()

    def manual_recording(self):
        selected = ''
        mtrs = []
        nonActive = []

        for motor in self.motors_:
            if self.check_button_value[motor].get():
                selected += motor
                selected += ' '
                mtrs.append(motor)
            else:
                nonActive.append(motor)

        if selected == '':
            tkMessageBox.showerror(title= 'Warning', message='You need to select at least ONE Actor!')
            return None
        if tkMessageBox.askyesno(title='Warning',
                              message='Warning: You selected folowing actors: ' + str(selected) + 'the rest of robot will be in mode "freeze" do you want to continue?'):


            rec_fram = Toplevel()
            rec_fram.grab_set()
            rec_fram.transient(self.master)
            # self.master.wait_window(RECD)
            #myRec = RECORDING_1(rec_fram, mtrs)



    def pos_by_pos_recording(self):
        selected = ''
        mtrs = []
        nonActive = []

        for motor in self.motors_:
            if self.check_button_value[motor].get():
                selected += motor
                selected += ' '
                mtrs.append(motor)
            else:
                nonActive.append(motor)

        if selected == '':
            #  tkMessageBox.ERROR
            tkMessageBox.showerror(title='Warning', message='You need to select at least ONE Actor!')
            return None
        if tkMessageBox.askyesno(title='Warning',
                                 message='Warning: You selected folowing actors: ' + str(
                                     selected) + 'the rest of robot will be in mode "freeze" do you want to continue?'):
            pos_rec_fram = Toplevel()
            pos_rec_fram.grab_set()
            pos_rec_fram.transient(self.master)
            # self.master.wait_window(RECD)
            #print mtrs
            #myPosRec = RECORDING_2(pos_rec_fram, mtrs)


    def editSign(self):
        recFile = tkFileDialog.askopenfilename(initialdir="/home/odroid/catkin_ws/src/robot_body/recording/data_base")
        if not recFile:
            return None
        print 'Openning the file: ' + recFile
        with open(recFile, "r") as sign:
            self.movement = json.load(sign)
        edit_fram = Toplevel()
        edit_fram.grab_set()
        edit_fram.transient(self.master)
        #handsSet = finger.__init__(edit_fram, self.movement, motor, pub)

    def __init__(self, master):
        self.master = master
        self.check_button_value = {}
        self.check_button={}
        self.master.title('Hi Poppy ;-)')
        self.new_sign_panel = LabelFrame(master, text="Record new sign")
        self.new_sign_panel.pack(fill="both", expand="yes")

        self.head = LabelFrame(self.new_sign_panel, text="Head")
        self.head.grid(row=0, column=1, rowspan=2)
        self.check_button_value["head"] = IntVar()
        self.check_button["head"] = Checkbutton(self.head, text = "", variable = self.check_button_value["head"], command= lambda: self.action("head"))
        self.check_button["head"].grid(row=0, column=0)
        self.check_button_value["head_y"] = IntVar()
        self.check_button["head_y"] = Checkbutton(self.head, text = "head_y", variable = self.check_button_value["head_y"])
        self.check_button["head_y"].grid(row=1, column=1, sticky=W)
        self.check_button_value["head_z"] = IntVar()
        self.check_button["head_z"] = Checkbutton(self.head, text = "head_z", variable =self.check_button_value["head_z"])
        self.check_button["head_z"].grid(row=2, column=1, sticky=W)

        self.manuel = Button(self.new_sign_panel, text="Manuel recording", width=15, command=self.manual_recording)
        self.manuel.grid(row=0, column=0)
        self.pos_by_pos = Button(self.new_sign_panel, text="Pos By Pos recording", width=15, command=self.pos_by_pos_recording)
        self.pos_by_pos.grid(row=1, column=0)


        self.torso = LabelFrame(self.new_sign_panel, text="Torso")
        self.torso.grid(row=2, column=1)
        self.check_button_value["torso"] = IntVar()
        self.check_button["torso"] = Checkbutton(self.torso, text = "", variable = self.check_button_value["torso"], command= lambda: self.action("torso"))
        self.check_button["torso"].grid(row=0, column=0)
        self.check_button_value["abs_z"] = IntVar()
        self.check_button["abs_z"] = Checkbutton(self.torso, text = "abs_z", variable = self.check_button_value["abs_z"])
        self.check_button["abs_z"].grid(row=1, column=1, sticky=W)
        self.check_button_value["bust_y"] = IntVar()
        self.check_button["bust_y"] = Checkbutton(self.torso, text = "bust_y", variable = self.check_button_value["bust_y"])
        self.check_button["bust_y"].grid(row=2, column=1, sticky=W)
        self.check_button_value["bust_x"] = IntVar()
        self.check_button["bust_x"] = Checkbutton(self.torso, text = "bust_x", variable = self.check_button_value["bust_x"])
        self.check_button["bust_x"].grid(row=3, column=1, sticky=W)



        self.R_arm = LabelFrame(self.new_sign_panel, text="R_arm")
        self.R_arm.grid(row=2, column=2, sticky=E)
        self.check_button_value["r_arm"] = IntVar()
        self.check_button["r_arm"] = Checkbutton(self.R_arm, text = "", variable = self.check_button_value["r_arm"], command= lambda: self.action("r_arm"))
        self.check_button["r_arm"].grid(row=0, column=0)
        self.check_button_value["r_shoulder_y"] = IntVar()
        self.check_button["r_shoulder_y"] = Checkbutton(self.R_arm, text = "r_shoulder_y", variable = self.check_button_value["r_shoulder_y"])
        self.check_button["r_shoulder_y"].grid(row=1, column=1, sticky=W)
        self.check_button_value["r_shoulder_x"] = IntVar()
        self.check_button["r_shoulder_x"] = Checkbutton(self.R_arm, text = "r_shoulder_x", variable = self.check_button_value["r_shoulder_x"])
        self.check_button["r_shoulder_x"].grid(row=2, column=1, sticky=W)
        self.check_button_value["r_arm_z"] = IntVar()
        self.check_button["r_arm_z"] = Checkbutton(self.R_arm, text = "r_arm_z", variable = self.check_button_value["r_arm_z"])
        self.check_button["r_arm_z"].grid(row=3, column=1, sticky=W)
        self.check_button_value["r_elbow_y"] = IntVar()
        self.check_button["r_elbow_y"] = Checkbutton(self.R_arm, text = "r_elbow_y", variable = self.check_button_value["r_elbow_y"])
        self.check_button["r_elbow_y"].grid(row=4, column=1, sticky=W)
        self.check_button_value["r_forearm_z"] = IntVar()
        self.check_button["r_forearm_z"] = Checkbutton(self.R_arm, text = "r_forearm_z", variable = self.check_button_value["r_forearm_z"])
        self.check_button["r_forearm_z"].grid(row=5, column=1, sticky=W)

        self.L_arm = LabelFrame(self.new_sign_panel, text="L_arm")
        self.L_arm.grid(row=2, column=0, sticky=E)
        self.check_button_value["l_arm"] = IntVar()
        self.check_button["l_arm"] = Checkbutton(self.L_arm, text = "", variable = self.check_button_value["l_arm"], command= lambda: self.action("l_arm"))
        self.check_button["l_arm"].grid(row=0, column=0)
        self.check_button_value["l_shoulder_y"] = IntVar()
        self.check_button["l_shoulder_y"] = Checkbutton(self.L_arm, text = "l_shoulder_y", variable = self.check_button_value["l_shoulder_y"])
        self.check_button["l_shoulder_y"].grid(row=1, column=1, sticky=W)
        self.check_button_value["l_shoulder_x"] = IntVar()
        self.check_button["l_shoulder_x"] = Checkbutton(self.L_arm, text = "l_shoulder_x", variable = self.check_button_value["l_shoulder_x"])
        self.check_button["l_shoulder_x"].grid(row=2, column=1, sticky=W)
        self.check_button_value["l_arm_z"] = IntVar()
        self.check_button["l_arm_z"] = Checkbutton(self.L_arm, text = "l_arm_z", variable = self.check_button_value["l_arm_z"])
        self.check_button["l_arm_z"].grid(row=3, column=1, sticky=W)
        self.check_button_value["l_elbow_y"] = IntVar()
        self.check_button["l_elbow_y"] = Checkbutton(self.L_arm, text = "l_elbow_y", variable = self.check_button_value["l_elbow_y"])
        self.check_button["l_elbow_y"].grid(row=4, column=1, sticky=W)
        self.check_button_value["l_forearm_z"] = IntVar()
        self.check_button["l_forearm_z"] = Checkbutton(self.L_arm, text = "l_forearm_z", variable = self.check_button_value["l_forearm_z"])
        self.check_button["l_forearm_z"].grid(row=5, column=1, sticky=W)

        self.motors_ = config.get_motor_list(config.robot_2_config)
        for name, param in self.check_button.items():
            if (param['text']!="") & (param['text'] not in self.motors_):
                param.config(state=DISABLED)



        self.edit_sign_panel = LabelFrame(master, text="Edit old sign")
        self.edit_sign_panel.pack(fill="both", expand="yes")
        self.loadFile = Button(self.edit_sign_panel, text="Load File", width=10, command=self.editSign)
        self.loadFile.pack()

        self.Close = Button(master, text="Close", width=10, command=self.Close_call)
        self.Close.pack(anchor=E)


root = Tk()
hi_poppy = MAIN(root)
root.mainloop()
