import cv2
import numpy as np
img = cv2.imread('rice.png', 0)
gamma_values = [0.1, 0.2, 0.8, 1.5, 3.5]
for gamma in gamma_values:
    gamma_img = np.power(img/255.0, gamma)
    cv2.imshow('Gamma = ' + str(gamma), gamma_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
