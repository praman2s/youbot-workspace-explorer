#!/usr/bin/env python
#
# Copyright 2013 _ArnO_. See the LICENSE file at the top-level directory of
# this distribution and at
# https://github.com/Arn-O/youbot-workspace-explorer/blob/master/LICENSE.

'''
This program generates a dict of reachable positions of the end-effector of
the KUKA youBot and dump the values into a flat file.
'''

import pickle
import math as m

# Global constants
PI = 3.1415926535897931
DELTA = 0.05

THETA_1_MIN = 0.0
THETA_1_MAX = (155.0 / 180) * PI
THETA_1_OFFSET = (155.0 / 180) * PI

THETA_2_MIN = (146.0 / 180) * PI * -1
THETA_2_MAX = (151.0 / 180) * PI
THETA_2_OFFSET = (146.0 / 180) * PI * -1

THETA_3_MIN = (102.5 / 180) * PI * -1
THETA_3_MAX = (102.5 / 180) * PI
THETA_3_OFFSET = (102.5 / 180) * PI

A_1 = 0.155
A_2 = 0.135
A_3 = 0.218

ARM_FRAM_X = 0.167
ARM_FRAM_Y = 0.192
WHEEL_OFFSET = 0.034
BASE_LENGTH = 0.570

def has_collided(coord):
    '''Check if the position is not a collision.'''
    (x, y) = coord
    if y < ((ARM_FRAM_Y + WHEEL_OFFSET) * -1):
        return True

    if y < 0 and x < ((BASE_LENGTH / 2) - ARM_FRAM_X) and x > (ARM_FRAM_X * -1):

        return True

    if y < (WHEEL_OFFSET * -1) and x  < (ARM_FRAM_X *
                    -1) and x > (((BASE_LENGTH / 2) + ARM_FRAM_X) * -1):
        return True

    return False

def theta_to_joint(theta):
    '''Convert theta in joints angles.'''
    # converted into integer to minimizing the volume
    joint_1 = int((theta[0] * -1 + THETA_1_OFFSET) * 100)
    joint_2 = int((theta[1] * -1 + THETA_2_OFFSET) * 100)
    joint_3 = int((theta[2] * -1 + THETA_3_OFFSET) * 100)
    return (joint_1, joint_2, joint_3)

def odom_frame_tf(coord):
    '''Frame transform to odom frame.'''
    (x, y) = coord
    # converted into integer to minimizing the volume
    x_odom = int((x + ARM_FRAM_X) * 1000)
    z_odom = int((y + ARM_FRAM_Y) * 1000)
    return (x_odom, z_odom)

def add_to_dict(iv, xz, joint):
    '''Add the coordination and joint tuples to the iv dict.'''
    if xz in iv:
        iv[xz].append(joint)
    else:
        iv[xz] = [joint]

def main():

    nb_iter_i = int((THETA_1_MAX - THETA_1_MIN) / DELTA) + 1
    nb_iter_j = int((THETA_2_MAX - THETA_2_MIN) / DELTA) + 1
    nb_iter_k = int((THETA_3_MAX - THETA_3_MIN) / DELTA) + 1
    nb_iter = nb_iter_i + nb_iter_j + nb_iter_k

    current_iter = 0
    iv = {}
    for i in range(nb_iter_i):
        theta_1 = THETA_1_MIN + DELTA * i
        
        ut_1 = theta_1
        x_1 = A_1 * m.cos(theta_1)
        y_1 = A_1 * m.cos(theta_1)

        for j in range(nb_iter_j):
            theta_2 = THETA_2_MIN + DELTA * j
        
            ut_12 = ut_1 + theta_2
            x_12 = x_1 + A_2 * m.cos(ut_12)
            y_12 = y_1 + A_2 * m.sin(ut_12)

            for k in range(nb_iter_k):
                theta_3 = THETA_3_MIN + DELTA * k
        
                ut_123 = ut_12 + theta_3
                x_123 = x_12 + A_3 * m.cos(ut_123)
                y_123 = y_12 + A_3 * m.sin(ut_123)
                    
                xy = (x_123, y_123)
                if has_collided(xy):
                    continue
                
                theta = (theta_1, theta_2, theta_3)
                
                joint = theta_to_joint(theta)
                xz = odom_frame_tf(xy)
                add_to_dict(iv, xz, joint)

    with open('inverse_kinematics.txt', 'wb') as handle:
        pickle.dump(iv, handle)
        
    print 'Done.'

if __name__ == '__main__':
    main()
