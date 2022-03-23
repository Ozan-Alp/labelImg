#!/usr/bin/env python
"""
Sample script that uses the libreducehaze module created using
MATLAB Compiler SDK.

Refer to the MATLAB Compiler SDK documentation for more information.
"""

from __future__ import print_function
import libreducehaze
import matlab

my_libreducehaze = libreducehaze.initialize()

filenameIn = "/home/ozan/Desktop/lol/0.jpg"
my_libreducehaze.reducehaze(filenameIn, nargout=0)

my_libreducehaze.terminate()
