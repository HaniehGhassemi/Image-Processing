import cv2
import numpy as np
import matplotlib.pyplot as plt

def calc_histogram(image):
    hist, _ = np.histogram(image.ravel(), bins=256, range=[0, 256])
    hist = hist / np.sum(hist)
    return hist

def calc_equalizer(hist):
    cdf = np.cumsum(hist)
    equalizer = np.round(cdf * 255).astype(int)
    return equalizer

# بارگذاری تصویر
image_path = 'home.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# بررسی موفقیت بارگذاری تصویر
if image is None:
    print(f"Could not read the image at path {image_path}")
else:
    # محاسبه هیستوگرام تصویر
    hist = calc_histogram(image)

    # محاسبه تابع هموارسازی
    equalizer = calc_equalizer(hist)

    # هموارسازی تصویر
    equalized_image = equalizer[image]

    # نمایش تصویر و هیستوگرام‌ها
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.imshow(image, cmap='gray')
    ax1.set_title('Original Image')
    ax2.imshow(equalized_image, cmap='gray')
    ax2.set_title('Equalized Image')
    plt.show()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.bar(np.arange(256), hist, width=1)
    ax1.set_xlabel('Pixel intensity')
    ax1.set_ylabel('Frequency')
    ax1.set_title('Original Image Histogram')
    ax2.bar(np.arange(256), calc_histogram(equalized_image), width=1)
    ax2.set_xlabel('Pixel intensity')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Equalized Image Histogram')
    plt.show()

    # نمایش تابع هموارسازی
    fig, ax = plt.subplots()
    ax.plot(np.arange(256), calc_equalizer(hist))
    ax.set_xlabel('Pixel intensity')
    ax.set_ylabel('Equalizer function value')
    ax.set_title('Histogram Equalization Function')
    plt.show()