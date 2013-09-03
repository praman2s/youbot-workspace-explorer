#!/usr/bin/env python
#
# Copyright 2013 _ArnO_. See the LICENSE file at the top-level directory of
# this distribution and at
# https://github.com/Arn-O/youbot-workspace-explorer/blob/master/LICENSE.

'''
This program generates and dict of reachable positions of the end-effector of
the KUKA youBot and dump the values into a flat file.
'''

import pickle

def main():

    with open('inverse_kinematics.txt', 'rb') as handle:
        iv = pickle.loads(handle.read())

    for coord in iv.keys():
        if len(iv[coord]) >= 7:
            print len(iv[coord]), coord, iv[coord]

if __name__ == '__main__':
    main()
