import numpy as np
import cv2
import matplotlib.pyplot as plt

# ---------- i) Image Translation ----------
input_img = cv2.imread("color image of flower.jpg")
input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)   # convert BGR → RGB for matplotlib

plt.axis('off')
plt.imshow(input_img)
plt.title("Original Image")
plt.show()

rows, cols, dim = input_img.shape

# Translation matrix: move 20px right, 50px down
M = np.float32([[1, 0, 20],
                [0, 1, 50]])

translated_img = cv2.warpAffine(input_img, M, (cols, rows))

plt.axis('off')
plt.imshow(translated_img)
plt.title("Translated Image")
plt.show()


# ---------- ii) Image Scaling ----------
# Scaling matrix (1.5x horizontally, 1.5x vertically)
scale_M = np.float32([[1.5, 0, 0],
                      [0, 1.5, 0]])

scaled_img = cv2.warpAffine(input_img, scale_M, (int(cols * 1.5), int(rows * 1.5)))

plt.axis('off')
plt.imshow(scaled_img)
plt.title("Scaled Image")
plt.show()


# ---------- iii) Image Shearing ----------
# Shear in X direction
M_x = np.float32([[1, 0.2, 0],
                  [0, 1, 0]])

# Shear in Y direction
M_y = np.float32([[1, 0, 0],
                  [0.2, 1, 0]])

sheared_img_xaxis = cv2.warpAffine(input_img, M_x, (cols, rows))
sheared_img_yaxis = cv2.warpAffine(input_img, M_y, (cols, rows))

plt.axis('off')
plt.imshow(sheared_img_xaxis)
plt.title("Sheared Image (X-axis)")
plt.show()

plt.axis('off')
plt.imshow(sheared_img_yaxis)
plt.title("Sheared Image (Y-axis)")
plt.show()
