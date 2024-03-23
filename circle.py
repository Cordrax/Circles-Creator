from PIL import Image
from math import *

radius = int(input("Entrer le rayon : "))
image_size = 4 * radius
im = Image.new("RGBA", (image_size, image_size), "white")
center_cos = int(c/2)
im.putpixel((center_cos, center_cos), (255,0,0))
for y in range(center_cos - radius, center_cos + radius):
        x = cen -1 - int(sqrt(radius**2 - ( y - center_cos)**2))
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
