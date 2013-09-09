#!/usr/bin/env python
#
# Copyright 2013 _ArnO_. See the LICENSE file at the top-level directory of
# this distribution and at
# https://github.com/Arn-O/youbot-workspace-explorer/blob/master/LICENSE.

'''
This program gives the inverse kinematics solutions for a given target for the
KUKA youBot.
'''

import pickle

UP_THETA_OFFSET = -3.52

def main():

    print 'Loading file ...'
    with open('inverse_kinematics.txt', 'rb') as handle:
        iv = pickle.loads(handle.read())
    print 'Done.'

    while True:
        print
        print 'Enter (0, 0) to quit.'
        coord = (input('x? '), input('y? '))
        if coord == (0, 0):
            break
    
        print 'Coordinates: ', coord
        if coord in iv.keys():
            print 'Number of solution(s): ', len(iv[coord])
            for joint_poses in iv[coord]:
                print '\t', 'Joints pose: ', joint_poses,
                up_theta = UP_THETA_OFFSET
                for joint_pose in joint_poses:
                    up_theta = up_theta + (float(joint_pose) / 100)
                print ' - orient.: ', up_theta
        else:
            print 'Not found'

    print 'Bye!'

if __name__ == '__main__':
    main()
