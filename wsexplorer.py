#!/usr/bin/env python
#
# Copyright 2013 _ArnO_. See the LICENSE file at the top-level directory of
# this distribution and at https://github.com/Arn-O/youbot-workspace-explorer/blob/master/LICENSE.

'''
This program generates and dict of reachable positions of the end-effector of
the KUKA youBot and dump the values into a flat file.
'''

import math as m

# Global constants
PI = 3.1415926535897931
DELTA = 0.5

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

def main():

    nb_iter_1 = int((THETA_1_MAX - THETA_1_MIN) / DELTA) + 1
    nb_iter_2 = int((THETA_2_MAX - THETA_2_MIN) / DELTA) + 1
    nb_iter_3 = int((THETA_3_MAX - THETA_3_MIN) / DELTA) + 1
    nb_iter = nb_iter_1 * nb_iter_2 * nb_iter_3
    current_iter = 0

    for i in range(nb_iter_1):
        theta_1 = THETA_1_MIN + DELTA * i
        x_1 = A_1 * m.cos(theta_1)
        y_1 = A_1 * m.cos(theta_1)
        ut_1 = theta_1

        for j in range(nb_iter_2):
            theta_2 = THETA_2_MIN + DELTA * j
            x_12 = x_1 + A_2 * m.cos(theta_1 + theta_2)
            y_12 = y_1 + A_2 * m.sin(theta_1 + theta_2)
            ut_12 = ut_1 + theta_2

            for k in range(nb_iter_3):
                current_iter += 1

                theta_3 = THETA_3_MIN + DELTA * k
                x_123 = x_12 + A_3 * m.cos(theta_1 + theta_2 + theta_3)
                y_123 = y_12 + A_3 * m.sin(theta_1 + theta_2 + theta_3)
                ut_123 = ut_12 + theta_3

                print ('Iter: %5i / % 5i - ' % (current_iter, nb_iter)),
                print ('t1: %.2f t2: %.2f t3: %.2f - x: %.3f y: %.3f' %                     (theta_1, theta_2, theta_3, x_123, y_123))
                
if __name__ == '__main__':
    main()
