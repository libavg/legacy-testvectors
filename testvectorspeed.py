#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import *
from libavg import *

global Player

XRANGE = (20, 1024-20)
YRANGE = (20, 768-20)

def addLines():
    canvas = Player.getElementByID("canvas")
    for i in xrange(200):
        line = Player.createNode("line", 
                {"x1":randrange(XRANGE[0], XRANGE[1]), 
                 "y1":randrange(YRANGE[0], YRANGE[1]),
                 "x2":randrange(XRANGE[0], XRANGE[1]), 
                 "y2":randrange(YRANGE[0], YRANGE[1]),
                 "width":randrange(1,5)})
        canvas.appendChild(line)
    print canvas.getNumChildren()
    if canvas.getNumChildren() > 20000:
        Player.stop()

Player = avg.Player()
Log = avg.Logger.get()
Log.setCategories(Log.APP |
                  Log.WARNING | 
                  Log.PROFILE |
#                 Log.PROFILE_LATEFRAMES |
                  Log.CONFIG
#                 Log.MEMORY  |
#                 Log.BLTS    
#                 Log.EVENTS| 
#                 Log.EVENTS2
                 )
Player.loadString("""
    <?xml version="1.0"?>
    <!DOCTYPE avg SYSTEM "../../doc/avg.dtd">
    <avg width="1024" height="768">
      <canvas id="canvas" width="1024" height="768"/>
    </avg>
""")
Player.setOnFrameHandler(addLines)
Player.setFramerate(60)
Player.play()


