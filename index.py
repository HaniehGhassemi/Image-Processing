import cv2
import numpy as np
import matplotlib.pyplot as plt

def calc_histogram(image):
    hist, _ = np.histogram(image.ravel(), bins=256, range=[0, 256])
    hist = hist / np.sum(hist)
    return hist

def draw_histogram(hist):
    bins = np.arange(257)
    fig, ax = plt.subplots()
    ax.set_xlabel('Pixel intensity')
    ax.set_ylabel('Frequency')
    ax.set_title('Grayscale Image Histogram')
    ax.bar(bins[:-1], hist, width=1)
    plt.show()

image = cv2.imread('home.png', cv2.IMREAD_GRAYSCALE)

hist = calc_histogram(image)

draw_histogram(hist)