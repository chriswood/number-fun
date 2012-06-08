#!/usr/bin/env python
# encoding: utf-8
"""
mac-int.py

Created by Chris Wood on 2012-05-28.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import Tkinter
from Tkinter import Tk, Label


def main():
    root = Tk()
    w=Label(root, text="Hey man this is a window")
    
    w.pack()
    w.mainloop()


if __name__ == '__main__':
    main()