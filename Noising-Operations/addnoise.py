import cv2
import numpy as np

# Read image
img = cv2.imread('happythumbs.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Add artificial blur
blurred_image = cv2.GaussianBlur(img_rgb, (5, 5), 0)

# Impulse noise
in_img = blurred_image.copy()
p = 0.1
for i in range(in_img.shape[0]):
    for j in range(in_img.shape[1]):
        r = np.random.rand()
        if r < p / 2:
            in_img[i, j] = [0, 0, 0]
        elif r < p:
            in_img[i, j] = [255, 255, 255]



# export image
cv2.imwrite('image_noise.jpg', cv2.cvtColor(in_img, cv2.COLOR_RGB2BGR))
