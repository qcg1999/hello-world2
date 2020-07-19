# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:32:24 2020

@author: Charlie
"""

import graphics.primitive.line as l
from graphics.primitive import fill as f
from graphics.primitive.text import text_1

import graphics as g
import graphics.formats.jpg
import graphics.formats.png as p

#once you have __init__.py
import graphics.formats as gf


def main():
    print("in main")
    l.line_1()
    f.fill_1()
    
    text_1()     #no leading name space
    
    g.formats.png.png_1()
    
    graphics.formats.jpg.jpg_1()  #must import graphics.formats.jpg
    
    p.png_1()
    
    gf.jpg.jpg_1()

    
    
    

# main
main()