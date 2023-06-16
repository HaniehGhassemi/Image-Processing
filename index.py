import numpy as np
import matplotlib.pyplot as plt

# تعریف ماتریس
matrix = np.array([[7, 3, 7, 6, 5, 5, 6, 2, 2, 1],
                   [1, 5, 6, 1, 2, 2, 2, 2, 7, 7],
                   [2, 1, 6, 4, 2, 3, 4, 2, 4, 3],
                   [3, 5, 3, 4, 4, 6, 6, 6, 6, 6],
                   [4, 6, 7, 3, 4, 5, 4, 5, 6, 4],
                   [6, 3, 2, 1, 7, 7, 4, 5, 6, 7],
                   [2, 1, 6, 4, 2, 3, 4, 2, 4, 3],
                   [1, 2, 2, 6, 5, 5, 6, 7, 3, 7],
                   [4, 6, 7, 3, 4, 5, 4, 5, 6, 4],
                   [6, 3, 2, 1, 7, 7, 4, 5, 6, 7]])

# محاسبه هیستوگرام اولیه
hist_before, _ = np.histogram(matrix.ravel(), bins=256, range=[0, 256])

# هموارسازی هیستوگرام
cdf = np.cumsum(hist_before)
cdf_normalized = cdf / cdf.max()
equalizer = np.round(cdf_normalized * 255).astype(int)
matrix_equalized = equalizer[matrix]

# محاسبه هیستوگرام هموارسازی شده
hist_after, _ = np.histogram(matrix_equalized.ravel(), bins=256, range=[0, 256])

# نمایش نمودار هیستوگرام‌ها
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.bar(np.arange(256), hist_before)
plt.title('Original Image Histogram')
plt.xlabel('Pixel intensity')
plt.ylabel('Frequency')
plt.subplot(122)
plt.bar(np.arange(256), hist_after)
plt.title('Equalized Image Histogram')
plt.xlabel('Pixel intensity')
plt.ylabel('Frequency')
plt.show()