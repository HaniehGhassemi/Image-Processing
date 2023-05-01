from PIL import Image
import numpy as np

img = Image.open('picture.jpg').convert('L')

np_img = np.array(img)

image_array = []
for i in range(len(np_img)):
    image_array.append([])
    for j in range(len(np_img[0])):
        binary_string = format(np_img[i][j], '08b')
        image_array[i].append(binary_string);


print(image_array)