import numpy as np
import cv2
import matplotlib.pyplot as plt

# ---------- iv) Image Reflection ----------
input_image = cv2.imread("got.jpg")
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

plt.axis("off")
plt.title("Original Image")
plt.imshow(input_image)
plt.show()

rows, cols, dim = input_image.shape

# Reflection across X-axis (vertical flip)
M_x = np.float32([[1, 0, 0],
                  [0, -1, rows]])

# Reflection across Y-axis (horizontal flip)
M_y = np.float32([[-1, 0, cols],
                  [0, 1, 0]])

reflected_img_xaxis = cv2.warpAffine(input_image, M_x, (cols, rows))
reflected_img_yaxis = cv2.warpAffine(input_image, M_y, (cols, rows))

plt.axis("off")
plt.title("Reflected Image (X-axis)")
plt.imshow(reflected_img_xaxis)
plt.show()

plt.axis("off")
plt.title("Reflected Image (Y-axis)")
plt.imshow(reflected_img_yaxis)
plt.show()



# ---------- v) Image Rotation ----------
input_image = cv2.imread("got.jpg")
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

rows, cols, _ = input_image.shape
angle = 45  # degrees
center = (cols / 2, rows / 2)

# Rotation matrix
M = cv2.getRotationMatrix2D(center, angle, 1)  # (center, angle, scale)
rotated_img = cv2.warpAffine(input_image, M, (cols, rows))

plt.axis("off")
plt.title("Rotated Image (45°)")
plt.imshow(rotated_img)
plt.show()



# ---------- vi) Image Cropping ----------
input_image = cv2.imread("got.jpg")
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

plt.axis("off")
plt.title("Original Image for Cropping")
plt.imshow(input_image)
plt.show()

# Crop region: [y1:y2, x1:x2]
cropped_img = input_image[100:300, 200:400]  # adjust as needed

plt.axis("off")
plt.title("Cropped Image")
plt.imshow(cropped_img)
plt.show()
