#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Chris Wood on 2012-05-22.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys


def main():
    for i in range(int(sys.argv[1])):
        print(fib(i))
    
def fib(n):
    return n if n in [0,1] else fib(n-1) + fib(n-2)

    
if __name__ == "__main__":
    sys.exit(main())
