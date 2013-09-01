#!/usr/bin/env python
#
# Copyright 2013 _ArnO_. See the LICENSE file at the top-level directory of
# this distribution and at https://github.com/Arn-O/youbot-workspace-explorer/blob/master/LICENSE.

'''
General description
'''

import numpy as np
import math as m

# Global constants
PI = 3.1415926535897931
DELTA = 0.1

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
    print "Nb of iteration for theta 1:", nb_iter_1
    print "Nb of iteration for theta 2:", nb_iter_2
    print "Nb of iteration for theta 3:", nb_iter_3
    print "Total number of steps:", nb_iter_1 * nb_iter_2 * nb_iter_3

    for i in range(nb_iter_1):
        theta_1 = THETA_1_MIN + DELTA * i
    

if __name__ == '__main__':
    main()
