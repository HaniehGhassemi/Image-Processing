import cv2
import numpy as np

def automatic_gamma_correction(image, gamma=1.0):
    # Step 2: Divide the image into smaller blocks
    block_size = 16
    h, w = image.shape[:2]
    blocks_v = h // block_size
    blocks_h = w // block_size
    
    # Step 3: Calculate the mean and variance of each block
    block_means = np.zeros((blocks_v, blocks_h))
    block_variances = np.zeros((blocks_v, blocks_h))
    for i in range(blocks_v):
        for j in range(blocks_h):
            block = image[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size]
            block_means[i, j] = np.mean(block)
            block_variances[i, j] = np.var(block)

    # Step 4: Divide the blocks into dark and bright sets based on their mean
    dark_blocks = []
    bright_blocks = []
    for i in range(blocks_v):
        for j in range(blocks_h):
            if block_means[i, j] < 128:
                dark_blocks.append((i, j))
            else:
                bright_blocks.append((i, j))

    # Step 5: Calculate the mean and variance of dark and bright sets
    dark_var = np.mean(block_variances[[i for i, j in dark_blocks], [j for i, j in dark_blocks]])
    bright_var = np.mean(block_variances[[i for i, j in bright_blocks], [j for i, j in bright_blocks]])

    # Step 6: Determine the gamma correction value based on the variances
    if dark_var < bright_var:
        gamma = gamma * np.sqrt(bright_var / dark_var)
    else:
        gamma = gamma * np.sqrt(dark_var / bright_var)

    # Apply gamma correction to the image
    corrected = np.power(image / 255.0, gamma) * 255.0
    corrected = corrected.astype(np.uint8)

    return corrected, gamma

# Load the image
image = cv2.imread('rice.png', cv2.IMREAD_GRAYSCALE)

# Apply automatic gamma correction with gamma = 1.0
corrected, gamma = automatic_gamma_correction(image, gamma=1.0)

# Display the original and corrected images
cv2.imshow('Original', image)
cv2.imshow('Corrected', corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the gamma value
print('Gamma:', gamma)