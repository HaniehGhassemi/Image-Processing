import cv2
import numpy as np

# Load the grayscale image
img = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)

# Convert to binary string and store in a list of lists
img_binary_strings = [[format(pixel, '08b') for pixel in row] for row in img]

# Create bit planes and show them
for m in range(8):
    bit_plane = [[string[0:(7-m)] + string[8-m:] for string in row] for row in img_binary_strings]
    bit_plane = np.array(bit_plane , dtype=np.uint8)
    cv2.imshow(f'Bit Plane {m}', bit_plane)

# Show the original image
cv2.imshow('image', img)

# Wait for a key press before closing the windows
cv2.waitKey(0)
cv2.destroyAllWindows()