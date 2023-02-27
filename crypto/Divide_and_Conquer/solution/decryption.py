# import Image
from PIL import Image

# open both photos
i1 = Image.open('img1.png')
i2 = Image.open('img2.png')

# get width and height
width1, height1 = i1.size

# open new image
i3 = Image.new('RGB', (width1, height1))

# load the pixels
pixels = i3.load()

# loop through all pixels
for i in range(width1):
    for j in range(height1):
        # xor the values
        x = i1.getpixel((i,j)) ^ i2.getpixel((i,j))

        # if all white then convert to black
        # if (x,y,z) == (255,255,255):
        #     (x,y,z) = (0,0,0)

        # put the new pixels in place
        i3.putpixel((i,j), x)

# save the image
i3.save("decrypt.png", "PNG")