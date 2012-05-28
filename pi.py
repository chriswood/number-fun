#!/usr/bin/env python
# encoding: utf-8
"""
pi.py

Created by Chris Wood on 2012-05-22.
"""

import sys
import argparse


def startup(kwargs):
    method = kwargs['method']
    log = kwargs['log']
    if 'iterations' in kwargs:
        n = kwargs['iterations']

    print("Settings: ")
    for key in kwargs.keys():
        print("    %s = %s" %(key, kwargs[key]))


def gl_pi(i):
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

        print('Pi ~= %s' %(pi))


def fraction_pi():
    '''
    Just return the first several pi estimates based on fractions.
    '''
    pass

if __name__ == "__main__":
    methods = ['gl', 'fr']
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
    parser.add_argument('--log', action='store_true', default=False)
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    startup(vars(args))
    sys.exit(0)
