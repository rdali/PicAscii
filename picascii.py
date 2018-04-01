#!/usr/bin/env python


    ####################################################################################################################################
    #                                                                                                                                  #
    #                                        PicAscii: Picasso in ASCII art; ASCII written by ASCII                                    #
    #                                                              Rola Dali                                                           #
    #                                              March 2018; Nothing interesting on TV...                                            #
    #                                                                                                                                  #
    ####################################################################################################################################


from __future__ import print_function
import numpy as np
import getopt
import sys



## define ASCII characters:
ascii = {
"A" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[0, 0, 0, 0, 0]
],

"B" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 0],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"C" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 1],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[0, 1, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"D" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"E" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"F" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"G" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[1, 0, 0, 0, 0],
[1, 0, 1, 1, 1],
[1, 0, 0, 0, 1],
[0, 1, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"H" : [
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[0, 0, 0, 0, 0]
],

"I" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"J" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[1, 0, 1, 0, 0],
[1, 1, 1, 0, 0],
[0, 0, 0, 0, 0]
],

"K" : [
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 1, 0],
[1, 1, 1, 0, 0],
[1, 0, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 0, 0, 0, 0]
],

"L" : [
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"M" : [
[0, 0, 0, 0, 0],
[1, 1, 0, 1, 1],
[1, 1, 0, 1, 1],
[1, 0, 1, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[0, 0, 0, 0, 0]
],

"N" : [
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 1],
[1, 1, 0, 0, 1],
[1, 0, 1, 0, 1],
[1, 0, 0, 1, 1],
[1, 0, 0, 0, 1],
[0, 0, 0, 0, 0]
],

"O" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"P" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 0],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"Q" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1],
[1, 0, 1, 0, 1],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 0]
],

"R" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 0],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 0],
[1, 0, 1, 0, 0],
[1, 0, 0, 1, 1],
[0, 0, 0, 0, 0]
],

"S" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 1],
[1, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 1],
[1, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"T" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0]
],

"U" : [
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"V" : [
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[0, 1, 0, 1, 0],
[0, 1, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0]
],

"W" : [
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 1, 0, 1],
[1, 0, 1, 0, 1],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0]
],

"X" : [
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 1, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 0, 0, 0, 0]
],

"Y" : [
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0]
],

"Z" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 1, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"a" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 0, 0],
[0, 0, 0, 1, 0],
[0, 1, 1, 1, 0],
[1, 0, 0, 1, 0],
[0, 1, 1, 0, 1],
[0, 0, 0, 0, 0]
],

"b" : [
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 1, 1, 0, 0],
[1, 0, 0, 1, 0],
[0, 1, 1, 0, 0],
[0, 0, 0, 0, 0]
],

"c" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"d" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 1],
[0, 0, 1, 1, 1],
[0, 1, 0, 0, 1],
[0, 0, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"e" : [
[0, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 0, 0, 1],
[0, 1, 1, 1, 0],
[0, 1, 0, 0, 0],
[0, 0, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"f" : [
[0, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 0, 0, 0],
[1, 1, 1, 0, 0],
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"g" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 0, 0, 1],
[0, 0, 1, 1, 1],
[0, 0, 0, 0, 1],
[0, 1, 1, 1, 0]
],

"h" : [
[0, 0, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 1, 0, 0, 1],
[0, 1, 0, 0, 1],
[0, 0, 0, 0, 0]
],

"i" : [
[0, 0, 0],
[0, 1, 0],
[0, 0, 0],
[0, 1, 0],
[0, 1, 0],
[0, 1, 0],
[0, 0, 0]
],

"j" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 1, 0],
[0, 1, 0, 1, 0],
[0, 1, 1, 0, 0]
],

"k" : [
[0, 0, 0, 0, 0],
[0, 1, 0, 0, 1],
[0, 1, 0, 1, 0],
[0, 1, 1, 0, 0],
[0, 1, 0, 1, 0],
[0, 1, 0, 0, 1],
[0, 0, 0, 0, 0]
],

"l" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 0]
],

"m" : [
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 1, 0, 0, 1],
[1, 0, 0, 1, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0]
],

"n" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 1, 1, 1, 0],
[1, 0, 0, 1, 0],
[1, 0, 0, 1, 0],
[0, 0, 0, 0, 0]
],

"o" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 0, 0, 1],
[0, 1, 0, 0, 1],
[0, 0, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"p" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 1, 0, 1, 0],
[0, 1, 1, 1, 0],
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0]
],

"q" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 1, 0, 1, 0],
[0, 1, 1, 1, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 1, 0]
],

"r" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 1, 0, 1, 1],
[0, 1, 1, 0, 0],
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"s" : [
[0, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 0, 1, 0],
[0, 1, 1, 0, 0],
[0, 0, 0, 0, 0]
],

"t" : [
[0, 0, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 1],
[0, 0, 0, 0, 0]
],

"u" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 1, 0, 0, 1],
[0, 1, 0, 0, 1],
[0, 1, 0, 0, 1],
[0, 0, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"v" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 1, 0, 1, 0],
[0, 1, 0, 1, 0],
[0, 1, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0]
],

"w" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 0, 1, 0, 1],
[1, 0, 1, 0, 1],
[0, 1, 0, 1, 0],
[0, 0, 0, 0, 0]
],

"x" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 1, 0, 0, 1],
[0, 0, 1, 1, 0],
[0, 0, 1, 1, 0],
[0, 1, 0, 0, 1],
[0, 0, 0, 0, 0]
],

"y" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 1, 0, 0, 1],
[0, 1, 0, 0, 1],
[0, 0, 1, 1, 1],
[0, 0, 0, 0, 1],
[0, 1, 1, 1, 0]
],

"z" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 1],
[0, 0, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 1, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"0" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"1" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"2" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 0],
[0, 0, 0, 0, 1],
[1, 1, 1, 1, 0],
[1, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0]
],

"3" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 0],
[0, 0, 0, 0, 1],
[0, 1, 1, 1, 1],
[0, 0, 0, 0, 1],
[1, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"4" : [
[0, 0, 0, 0, 0],
[1, 0, 0, 1, 0],
[1, 0, 0, 1, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 1, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 0]
],

"5" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 0],
[1, 1, 1, 1, 0],
[0, 0, 0, 0, 1],
[1, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"6" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[1, 0, 0, 0, 0],
[1, 1, 1, 1, 0],
[1, 0, 0, 0, 1],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"7" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 1, 0, 0, 0],
[1, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"8" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"9" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1],
[0, 1, 1, 1, 1],
[0, 0, 0, 0, 1],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
],

"microSpace" : [
[0],
[0],
[0],
[0],
[0],
[0],
[0]
],

"miniSpace" : [
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0]
],

"medSpace" : [
[0, 0, 0],
[0, 0, 0],
[0, 0, 0],
[0, 0, 0],
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]
],

"Space" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"?" : [
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 0],
[0, 0, 0, 0, 1],
[0, 1, 1, 1, 0],
[1, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 0]
],

"," : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 1, 0, 0],
[1, 1, 1, 0, 0],
[0, 1, 0, 0, 0],
[1, 0, 0, 0, 0]
],

"@" : [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[1, 0, 1, 0, 1],
[1, 1, 0, 0, 1],
[1, 0, 1, 1, 0],
[1, 0, 0, 0, 0],
[0, 1, 1, 1, 0]
],

"#" : [
[0, 1, 0, 1, 0],
[0, 1, 0, 1, 0],
[1, 1, 1, 1, 1],
[0, 1, 0, 1, 0],
[1, 1, 1, 1, 1],
[0, 1, 0, 1, 0],
[0, 1, 0, 1, 0]
],

"^" : [
[0, 0, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 1, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"(" : [
[0, 0, 1, 0, 0],
[0, 1, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 0, 1, 0, 0]
],

")" : [
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 1],
[0, 0, 0, 1, 0],
[0, 0, 1, 0, 0]
],

"[" : [
[1, 1, 1, 0, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 0],
[1, 1, 1, 0, 0]
],

"]" : [
[0, 0, 1, 1, 1],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 1],
[0, 0, 1, 1, 1]
],

"-" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"_" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1]
],

"+" : [
[0, 0, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0]
],

"=" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"*" : [
[0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0, 0],
[1, 1, 1, 1, 1, 1, 1],
[0, 0, 1, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0]
],

"%" : [
[1, 1, 0, 0, 0, 0, 1],
[1, 1, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 1, 1],
[1, 0, 0, 0, 0, 1, 1]
],

"$" : [
[0, 0, 1, 0, 0],
[0, 1, 1, 1, 1],
[1, 0, 1, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 1, 0, 1],
[1, 1, 1, 1, 0],
[0, 0, 1, 0, 0]
],

"\'" : [
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 1],
[0, 0, 1, 1, 0],
[0, 1, 1, 0, 0],
[1, 1, 0, 0, 0],
[1, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"\"" : [
[0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1],
[0, 1, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0]
],

"&" : [
[0, 1, 1, 1, 1, 0, 0],
[1, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0, 0],
[1, 0, 0, 0, 1, 0, 0],
[1, 0, 1, 0, 1, 0, 0],
[1, 0, 0, 1, 1, 0, 0],
[0, 1, 1, 1, 0, 1, 1]
],

"\'" : [
[0, 0, 0, 0, 1],
[0, 0, 0, 1, 0],
[0, 0, 1, 1, 1],
[0, 0, 1, 1, 1],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"/" : [
[0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0]
],

"\\" : [
[1, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 1]
],

"<" : [
[0, 0, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 1, 0, 0, 0],
[1, 0, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 0]
],

">" : [
[0, 1, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 1],
[0, 0, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 1, 0, 0, 0]
],

"|" : [
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0]
],

"`" : [
[1, 0, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 1, 1, 0, 0],
[0, 0, 1, 1, 0],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
],

"{" : [
[0, 0, 0, 1, 1],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[1, 1, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 1]
],

"}" : [
[1, 1, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 1],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[1, 1, 0, 0, 0]
],

"~" : [
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]
],

"!" : [
[0, 0],
[1, 1],
[1, 1],
[1, 1],
[0, 0],
[1, 1],
[0, 0]
],

"." : [
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[1, 1],
[1, 1],
[0, 0]
],

":" : [
[0, 0],
[1, 1],
[1, 1],
[0, 0],
[1, 1],
[1, 1],
[0, 0]
],

";" : [
[0, 1, 1, 0, 0],
[0, 1, 1, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 1, 0, 0],
[1, 1, 1, 0, 0],
[0, 1, 0, 0, 0],
[1, 0, 0, 0, 0]
]
}

## render strings:


def codeString(myString = "PicASCII!!", Wspace = "Space", Lspace = "miniSpace", indent = 0):
    '''Method that codes strings into numpy array with vertically staggard letters'''
    codedString = np.array([])
    space_stag = np.concatenate((np.array(ascii[Lspace]), np.zeros((indent, np.array(ascii[Lspace]).shape[1]))) , axis = 0)
    for index, char in enumerate(myString):
        if char == " ":
            char = Wspace
        if char not in ascii.keys():
            char = Wspace
        if not (index % 2):
            char_arr = np.array(ascii[char])
            char_stag = np.concatenate((char_arr, np.zeros((indent, char_arr.shape[1]))) , axis = 0)
        else:
            char_arr = np.array(ascii[char])
            char_stag = np.concatenate((np.zeros((indent, char_arr.shape[1])), char_arr) , axis = 0)

        if index == 0:
            codedString = char_stag
        else:
            codedString = np.concatenate((codedString, space_stag, char_stag) , axis = 1)
    return codedString



## print:
def blockPrint(codedString, fill = "@", empty = " "):
    ''' Method that prints out array'''
    for row in codedString:
        for pos in row:
            if pos == 1:
                print(fill, end='')
            elif pos == 2:
                print(decorate, end='')
            elif pos == 3:
                print(begin, end='')
            else:
                print(empty, end='')
        print()


def check_letters(fill = "@", empty = " "):
    '''Method to print out available ASCII characters using chosen text and space filler'''
    myString1 = "Aa Bb Cc Dd Ee Ff Gg"
    myString2 = "Hh Ii Jj Kk Ll Mm Nn"
    myString3 = "Oo Pp Qq Rr Ss Tt Uu"
    myString4 = "Vv Ww Xx Yy Zz"
    myString5 = "0 1 2 3 4 5 6 7 8 9"
    myString6 = "! \" # $ % & '"
    myString7 = "( ) * + , - . /"
    myString8 = ": ; < = > ? ~ \ "
    myString9 = "[ ] ^ _ ` { | }"

    strings = [myString1, myString2, myString3, myString4, myString5, myString6, myString7, myString8, myString9]

    for myString in strings:
        codedString = codeString(myString)
        blockPrint(codedString, fill, empty)
        print()
        print()

def run_picascii(myString = "PicASCII!!", text= "%", filler= " ", mode = "norm", case= "norm", indent = 0):
    ''' main methode to code and print string'''
    if mode == "avail":
        check_letters(text, filler)
        sys.exit()

    if case == "up":
        myString = myString.upper()
    elif case == "lo":
        myString = myString.lower()

    if mode == "norm":
        Wspace = "Space"
        Lspace = "miniSpace"
        L_indent = 0
    elif mode == "sq":
        Wspace = "medSpace"
        Lspace = "microSpace"
        L_indent = 0
    elif mode == "stag":
        Wspace = "Space"
        Lspace = "miniSpace"
        L_indent = indent
    elif mode == "ss":
        Wspace = "medSpace"
        Lspace = "microSpace"
        L_indent = indent

    codedString = codeString(myString = myString, Wspace = Wspace, Lspace = Lspace, indent = L_indent)

    ## frame
    k = 3; #buffer btn text and frame
    if (decorate != "None"):
        codedString = np.concatenate((np.zeros((codedString.shape[0], k)), codedString), axis = 1)
        codedString = np.concatenate((codedString, np.zeros((codedString.shape[0], k))), axis = 1)
        codedString = np.concatenate((np.zeros((k, codedString.shape[1])), codedString), axis = 0)
        codedString = np.concatenate((codedString, np.zeros((k, codedString.shape[1]))), axis = 0)
        codedString[:,0] = 2
        codedString[0,:] = 2
        codedString[:,-1] = 2
        codedString[-1,:] = 2

    ## comment
    if (begin != "None"):
        codedString = np.concatenate((np.zeros((codedString.shape[0], 2)), codedString), axis = 1)
        codedString[:,0] = 3


    blockPrint(codedString, text, filler)


def print_args():
    print("myString:  " + myString)
    print("text:  " + text)
    print("filler:  " + filler)
    print("mode:  " + mode)


def help():
    '''Methods that prints out help message'''
    print ('''
    ----------------------------------------------------------------------------------------------
                                                  HELP
    ----------------------------------------------------------------------------------------------


    PicASCII.py draws your ASCII string using ASCII characters to be added in text files!
    US-ASCII letters:
    !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~


    usage: PicASCII.py -s myString [options]

    -s myString: a string made of ASCII letters.
                 To code newlines use "\\"
                             ~~~ Allowed letters: ~~~
                 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO
                 PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

    -t text:     a character used to fill in the text. Default = "@"
                             ~~~ Allowed letters: ~~~
                 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO
                 PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

    -f filler:   a character used to fill in spaces in the text. Default = " "
                             ~~~ Allowed letters: ~~~
                 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO
                 PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

    -m mode:     mode used to print characters. Default: "norm"
                                ~~~ options: ~~~
                avail: print out of available letters in the used text and filler
                norm: normal: letters printed with some spacing between letters
                stag: staggard: letters are staggared verically
                sq  : squish  : normal printing, less spaces between letters
                ss  : satggard & squished: letters are staggared and squished
    -i indent   indent = integer: is the stagger indentation.
                ONLY used if mode = stag or ss. Default = 2.
    -c case     mode used to print characters. Default: "norm"
                up: Upper Caps: prints all letters as capital letters
                lo: lower Caps: prints all letters as lower case letters
    -b begin    a character added to the beginning of a line, usually a comment
                character.

    -d decorate character to be used for frame


    ''')

## main:
try:
    options,remainder = getopt.getopt(sys.argv[1:],'s:t:f:m:c:i:b:d:h',["myString=","text=","filler=","mode=","case=","indent=","begin=","decorate=","help"])
except getopt.GetoptError, e:
    print ('usage: PicASCII.py -s myString [options]')
    print ("Error - "+str(e)+". See help ('-h' or '--help')")
    sys.exit(2)

## defaults:
myString = '~ WELCOME TO PicASCII ~'
text = "%"
filler = " "
mode = "norm"
case = "norm"
indent = 2
begin = "None"
decorate = "None"

## command line variables:
for opt,arg in options:
    if(opt in ["-s","--myString"]):
        myString=arg
    elif(opt in ["-t","--text"]):
        text=arg
    elif(opt in ["-f","--filler"]):
        filler=arg
    elif(opt in ["-m","--mode"]):
        mode=arg
        if mode not in ["avail", "norm", "stag", "sq", "ss"]:
            print ("The chosen mode is not available. please choose one of the following: {'avail', 'norm', 'stag', 'sq', 'ss'}")
            print ("Defaulting mode to 'norm'")
            mode = "norm"
    elif(opt in ["-c","--case"]):
        case=arg
        if case not in ["norm", "up", "lo"]:
            print ("The chosen case is not available. please choose one of the following: {'norm', 'up', 'lo'}")
            print ("Defaulting case to 'norm'")
            case = "norm"
    elif(opt in ["-i","--indent"]):
        try:
            indent = int(arg)
        except ValueError:
            print ('-i should be an integer number; defaulting to 2')
    elif(opt in ["-h","--help"]):
        help()
        sys.exit()
    elif(opt in ["-b","--begin"]):
        begin=arg
    elif(opt in ["-d","--decorate"]):
        decorate=arg

#print_args()

############# Add comment parameter: if comment add // or # at beginning of line
############# Add framing parameter: if frame, add frame around word

## run Picascii
myString = myString.split("\\")

for s in myString:
    run_picascii(myString = s, text= text, filler= filler, mode = mode, case= case, indent = indent)
    print()

if (myString[0] is '~ WELCOME TO PicASCII ~'):
    help()


print('''
    ----------------------------------------------------------------------------------------------
                                     PicASCII is complete!
                            Rola Dali; 2018; https://github.com/rdali
                           OPEN SOURCE: use, test, modify, distribute!
    ----------------------------------------------------------------------------------------------
''')