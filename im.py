import numpy as num
from PIL import Image
from matplotlib import cm

img = Image.open("test.jpg")

#quantization = num.array(img.convert('P', palette=Image.ADAPTIVE, colors=256))

max = num.amax(quantization)
min = num.amin(quantization)
range = max - min 

normalized = []
for row in quantization:
    newrow = []
    for val in row:
        newrow.append((val - min) / float(range))
    normalized.append(newrow)

#new = Image.fromarray(a)
new = Image.fromarray(num.uint8(cm.rainbow(normalized)*255))

new.save("out.bmp")
