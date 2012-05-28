#!/usr/bin/env python
# encoding: utf-8
"""
pi.py

Created by Chris Wood on 2012-05-22.
"""

import sys


def main():
    print('===========\n')
    pi(int(sys.argv[1]))
    print('===========\n')

#Gregory–Leibniz series
def pi(i):
    # set initial value (constant out of series. if any)
    pi = 0.0
    divisor = 4.0
    for iteration, value in enumerate(range(1, 2*i, 2), 1):
        print('iteration - %s' %(iteration))
        dividend = float(value)
        if iteration & 1: # is odd number
            pi += divisor/dividend
        else:
            pi -= divisor/dividend

        print('Pi = %s' %(pi))
    
if __name__ == "__main__":
    sys.exit(main())
