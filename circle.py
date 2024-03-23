from PIL import Image
from math import *

r = int(input("Entrer le rayon : "))
c = 4 * r
im = Image.new("RGBA", (c,c), "white")
cen = int(c/2)
ep = 0
im.putpixel((cen,cen), (255,0,0))
for y in range(cen-r, cen+r):
        x = cen -1 - int(sqrt(r**2 - (y-cen)**2))
        print(x)
        im.putpixel((x,y), (0,0,0))
        im.putpixel((-x,y), (0,0,0))
        im.putpixel((x,-y), (0,0,0))
        im.putpixel((-x,-y), (0,0,0))
        im.putpixel((y,x), (0,0,0))
        im.putpixel((-y,x), (0,0,0))
        im.putpixel((y,-x), (0,0,0))
        im.putpixel((-y,-x), (0,0,0))

im.show()
im.save("circle.png")
