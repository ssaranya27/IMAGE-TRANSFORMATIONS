import cv2
import numpy as np
import matplotlib.pyplot as plt
# --------------------- Helper Function ---------------------
def show_image(img, title="Image"):
    """
    Display an image using matplotlib with proper RGB conversion.
    """
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')

# --------------------- Load Image ---------------------
image = cv2.imread('image.jpg')  # Replace with your image path

if image is None:
    print("Error: Image not found")
else:
    (h, w) = image.shape[:2]

  # --------------------- 1. Translation ---------------------
  tx, ty = 100, 50  # Move 100 pixels right and 50 pixels down
  translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
  translated = cv2.warpAffine(image, translation_matrix, (w, h))

    # --------------------- 2. Scaling ---------------------
    # Resize by 1.5x horizontally and 0.75x vertically
    scaled = cv2.resize(image, None, fx=1.5, fy=0.75, interpolation=cv2.INTER_LINEAR)



 # --------------------- 3. Shearing ---------------------
    # Horizontal shear
shear_matrix_x = np.float32([[1, 0.5, 0], [0, 1, 0]])
sheared_x = cv2.warpAffine(image, shear_matrix_x, (int(w + 0.5*h), h))


