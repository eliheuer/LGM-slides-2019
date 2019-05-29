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

# PAGE ZERO ####################################################################
newPage(W, H)
fill(0.1)
rect(0, 0, W, H)
#font("source/fonts/Inter-Black.ttf")  # Set the font
font("Optima Bold")  # Set the font
#grid() # Toggle for grid view
#edge() # Toggle for safe area

image("source/images/cli-01.png", (-19, 0), alpha=1)

fill(1)
stroke(None)
fontSize(120)
#tracking(-4.5)
text("FONT BAKERY", M+96, M*20)
fontSize(49.5)
#tracking(-2.5)
text("Quality Assurance for Font Families", M+96, M*18)
saveImage("fontbakery-00.png")

# PAGE ONE #####################################################################
newPage(W, H)
grid() # Toggle for grid view
edge() # Toggle for safe area
text("Foo Bard", M, M*16)
image("source/images/cli-02.png", (-19, 0), alpha=1)
saveImage("fontbakery-01.png")
