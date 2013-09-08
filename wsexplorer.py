#!/usr/bin/env python
#
# Copyright 2013 _ArnO_. See the LICENSE file at the top-level directory of
# this distribution and at
# https://github.com/Arn-O/youbot-workspace-explorer/blob/master/LICENSE.

'''
This program generates a plot of the number for inverse kinematics solutions
for a given position of the gripper of the KUKA youBot.
'''

import matplotlib.pyplot as plt
import numpy as np
import pickle

def main():

    print 'Loading file ...'
    with open('inverse_kinematics.txt', 'rb') as handle:
        iv = pickle.loads(handle.read())
    print 'Done.'

    coord_x = []
    coord_y = []

    for coord in iv.keys():
        for _ in range(len(iv[coord])):
            coord_x.append(coord[0])
            coord_y.append(coord[1])

    x = np.array(coord_x)
    y = np.array(coord_y)

    xmin = x.min()
    xmax = x.max()
    ymin = y.min()
    ymax = y.max()

    gridsize=60

    plt.hexbin(x, y, gridsize=gridsize, cmap=plt.cm.jet, bins=None)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.subplot(111)
    cb = plt.colorbar()

    plt.show()

if __name__ == '__main__':
    main()
