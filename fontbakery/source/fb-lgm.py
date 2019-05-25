# Render this document with DrawBot3: http://www.drawbot.com/
from drawBot import *
import math

# Width, Height, Margin
W, H, M = 1024, 768, 32

def edge():
    #960, 704
    stroke(1,0,0)
    fill(None)
    rect(M, M, 960, 704)

def grid():
    stroke(0.3)
    stpX, stpY = 0, 0
    incX, incY = 32, 32
    for x in range(30):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(20):
        polygon((M, M+stpY), (W-M, M+stpY))
        stpY += incY

# PAGE ONE #####################################################################
newPage(W, H)
fill(0.1)
rect(0, 0, W, H)
font("source/fonts/Blob-Black.ttf")  # Set the font
#grid() # Toggle for grid view
#edge() # Toggle for safe area

image("source/images/cli-01.png", (-19, -25), alpha=1)

fill(1)
stroke(None)
fontSize(202)
text("FONT BAKERY", M, M*18)
fontSize(69)
#tracking(-2.5)
text("QUALITY ASSUrANCE FOr FONT FAMILIES", M, M*16)

saveImage("fontbakery-01.png")

# PAGE TWO #####################################################################
newPage(W, H)
image("source/images/cli-01.png", (-50, 0), alpha=1)
saveImage("fontbakery-02.png")
