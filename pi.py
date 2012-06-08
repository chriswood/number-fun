#!/usr/bin/env python
# encoding: utf-8
"""
pi.py

Created by Chris Wood on 2012-05-22.
"""

import sys
import argparse
from math import pi as py_pi


def startup(kwargs):
    '''
    Figure out what type of calculation we are dealing with and
    intsantiate the approprite class (just pi for now)
    '''
    method = kwargs['method']
    n = kwargs['iterations'] if 'iterations' in kwargs else None
    pi_67 = '3.1415926535897932384626433832795028841971693993751058209749445923078'

    calc = PiCalc(method=method, n=n)
    print("Settings: ")
    for key in kwargs.keys():
        print("    %s = %s" %(key, kwargs[key]))
    print("python to 67 digits = %s" %(pi_67))
    print("python's value of pi (via math.pi) %s "%(py_pi))
    print("%s's method to %s iterations result %s" %(method, n, calc.result))

class PiCalc(object):
    """
    Hold various methods for calculating Pi, as well well as
    comparing results, displaying iteration values, etc...
    """
    def __init__(self, method, n):
        super(PiCalc, self).__init__()
        method = "%s_pi" %(method)
        f = getattr(self, method)
        # TODO make this long
        self.result = f(n)

    def gl_pi(self, i):
        '''
        Return #Gregory–Leibniz series value
        '''
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

        return pi

    def nilakantha_pi(self, i):
        pi = 0.0
        constant = 3.0
        divisor = 4.0
        pi += constant
        for iteration, value in enumerate(range(2, (2*i)+1, 2), 1):
            denominator = value * (value + 1) * (value + 2)
            print("iteration = %s" %(iteration))
            if iteration & 1: # is odd number
                pi += divisor/denominator
            else:
                pi -= divisor/denominator

            print('Pi = %s' %(pi))
        return pi

    def fraction_pi(self):
        '''
        Just return the first several pi estimates based on fractions.
        '''
        pass


if __name__ == "__main__":
    methods = ['gl', 'fr', 'nilakantha']
    iter_help = 'For series calculations, the number of iterations must be > 0'
    log_help = '--log enables output for each iteration of infinte series'
    method_help = 'Choose from (gl - Gregory–Leibniz series, \n\
     fr - calculations of various fraction that closely estimate pu'
    parser = argparse.ArgumentParser(description='Script %(prog)s -\
        Calculate Pi using various methods', add_help=True)

    parser.add_argument('method', action='store', choices=methods, \
                         help=method_help)
    parser.add_argument('--iterations', action='store', type=int, \
                        help=iter_help, default=1)
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    startup(vars(args))
    sys.exit(0)
