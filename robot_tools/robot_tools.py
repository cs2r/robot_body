#!/usr/bin/python
# -*- coding: UTF-8 -*-  # this is to add arabic coding to python

import time
from robot_body.msg import motorSet
motor = motorSet()
right_hand = [200, 200, 100, 100, 200, 100, 100, 100, 100]
left_hand = [200, 200, 100, 100, 200, 100, 100, 100, 100]

def releas(names, pub, present_pos=None, L=None, R=None):
    if present_pos is not None:
        goal_position = {"Robot": [-15 if name == "bust_y" else 0 for name in names],
                         'Right_hand': right_hand, 'Left_hand': left_hand}
        go_to_pos(names, present_pos, goal_position, pub)
    for name in names:
        motor.compliant = True
        pub[name].publish(motor)
    if (L is not None) & (R is not None):
        multi_servo_set([0]*9, [0]*9, L, R)

def reset(names, motor_pos, pub):
    goal_position = {"Robot": [0 for name in names],
                     "Right_hand": right_hand,
                     "Left_hand": left_hand}
    go_to_pos(names, motor_pos, goal_position, pub)
#    for name in names:
#        motor.compliant = False
#        motor.goal_position = 0
#        pub[name].publish(motor)

def do_seq(names, freq, seq, pub, L=None, R=None, HEAD=None, emotion=None):
    if (HEAD is not None) & (emotion is not None):
        HEAD.publish(emotion)
    for frame in range(len(seq)):
        id = 0
        for name in names:
            motor.compliant = False
            motor.goal_position = seq[str(frame)]['Robot'][id]
            pub[name].publish(motor)
            id += 1
        if (L is not None) | (R is not None):
            multi_servo_set(seq[str(frame)]['Left_hand'], seq[str(frame)]['Right_hand'], L, R)
        time.sleep(1 / float(freq))

def build_seq(curent_pos, pos, max_err):
    pre_sign = {}
    frames = [float(x) / max_err for x in range(max_err + 1)]
    i = 0
    for frame in frames:
        pre_sign[str(i)] = {
            'Robot': [curent_pos["Robot"][ndx] + frame * frame * (3 - 2 * frame) * (pos["Robot"][ndx] - curent_pos["Robot"][ndx])
                      for ndx in range(len(pos["Robot"]))],
            'Right_hand': [curent_pos["Right_hand"][ndx] + frame * frame * (3 - 2 * frame) * (pos["Right_hand"][ndx] - curent_pos["Right_hand"][ndx])
                           for ndx in range(len(pos["Right_hand"]))],
            'Left_hand': [curent_pos["Left_hand"][ndx] + frame * frame * (3 - 2 * frame) * (pos["Left_hand"][ndx] - curent_pos["Left_hand"][ndx])
                           for ndx in range(len(pos["Left_hand"]))]}
        i += 1
    return pre_sign

def build_sign(first_pos, final_pos, init_fram, max_err, method="Smooth"):
    pre_sign = {}
    frames = [float(x) / max_err for x in range(max_err + 1)]
    i = init_fram
    for frame in frames:
        pre_sign[str(i)] = {
            'Robot': [first_pos[ndx] + frame * frame * (3 - 2 * frame) * (final_pos[ndx] - first_pos[ndx]) if method == "Smooth" else
                      (1 - frame) * first_pos[ndx] + frame * final_pos[ndx] for ndx in range(len(final_pos)) ],
            'Right_hand': [200, 200, 100, 100, 200, 100, 100, 100, 100],
            'Left_hand': [200, 200, 100, 100, 200, 100, 100, 100, 100]}
        i += 1
    return pre_sign

def go_to_pos(motors, motor, goal_position, pub, L=None, R=None, left_hand=None, right_hand=None):
    err_max = 5
    try:
        present_position = {"Robot": [motor[name].present_position for name in motors],
                            "Right_hand": right_hand if right_hand is not None else [200, 200, 100, 100, 200, 100, 100, 100, 100],
                            "Left_hand": left_hand if left_hand is not None else [200, 200, 100, 100, 200, 100, 100, 100, 100]}
        max_err = 0
        for id in range(len(goal_position["Robot"])):
            max_err = max([abs(goal_position["Robot"][id] - present_position["Robot"][id]), max_err])
        if max_err > err_max:
            print 'Going to pos'
            preset = build_seq(present_position, goal_position, int(max_err))
            do_seq(motors, max_err, preset, pub, L, R)
        else:
            print 'robot in pos'
            pos = {'0':goal_position}
            do_seq(motors, 100, pos, pub)
    except Exception, err:
        print 'Robot can go, error is '
        print err

def multi_servo_set(Lcommand=None, Rcommand=None, L=None, R=None):

    if (Lcommand is not None) & (L is not None):
        for servo in range(1,10):
            L[servo].publish(Lcommand[servo - 1])
    if (Rcommand is not None) & (R is not None):
        for servo in range(1,10):
            R[servo].publish(Rcommand[servo - 1])

def right_servo_set(servo, cmd, R):
    R[servo].publish(cmd)

def left_servo_set(servo, cmd, L):
    L[servo].publish(cmd)