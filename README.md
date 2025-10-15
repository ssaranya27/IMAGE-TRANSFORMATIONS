# IMAGE-TRANSFORMATIONS


## Aim
To perform image transformation such as Translation, Scaling, Shearing, Reflection, Rotation and Cropping using OpenCV and Python.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1: 
Import required libraries: numpy, cv2, and matplotlib.pyplot.
<br>
### Step2:
Read the input image and convert it from BGR to RGB format.
<br>
### Step3:
Apply image transformations — translation, scaling, shearing, reflection, rotation, and cropping.
<br>
### Step4:
Use appropriate transformation matrices with cv2.warpAffine() for each operation.
<br>
### Step5:
Display the original and transformed images using matplotlib.pyplot.imshow().
<br>

## Program:
```python
Developed By: SARANYA S
Register Number: 212223220101
```
i)Image Translation
```
import numpy as np
import cv2
import matplotlib.pyplot as plt
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
```
ii) Image Scaling
```
# Scaling matrix (1.5x horizontally, 1.5x vertically)
scale_M = np.float32([[1.5, 0, 0],
                      [0, 1.5, 0]])

scaled_img = cv2.warpAffine(input_img, scale_M, (int(cols * 1.5), int(rows * 1.5)))

plt.axis('off')
plt.imshow(scaled_img)
plt.title("Scaled Image")
plt.show()
```
iii)Image shearing
```
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
```
iv)Image Reflection
```
import numpy as np
import cv2
import matplotlib.pyplot as plt

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
```
v)Image Rotation
```
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
```
vi)Image Cropping
```
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
```


## Output:
### i)Image Translation
## Original:
<br>
<img width="311" height="530" alt="Screenshot 2025-10-15 210135" src="https://github.com/user-attachments/assets/7b58c166-3494-42d5-92c2-72b2dedf5765" />
<br>
<br>
<img width="329" height="534" alt="Screenshot 2025-10-15 210156" src="https://github.com/user-attachments/assets/245c3ae1-9677-499a-8d29-e15310ae9331" />
<br>

## ii) Image Scaling
<br>
<img width="301" height="529" alt="Screenshot 2025-10-15 210219" src="https://github.com/user-attachments/assets/6e0b83ff-134f-478f-a0d3-94b6599ac978" />
<br>

## iii)Image shearing
<br>
<img width="312" height="527" alt="Screenshot 2025-10-15 210239" src="https://github.com/user-attachments/assets/148f05e0-b3e2-47b4-be31-31533cb2101c" />
<br>
<br>
<img width="319" height="507" alt="Screenshot 2025-10-15 210255" src="https://github.com/user-attachments/assets/e9bed823-5cce-46a2-a710-613eafb0825c" />
<br>
## iv)Image Reflection
<br>
<img width="299" height="527" alt="Screenshot 2025-10-15 210326" src="https://github.com/user-attachments/assets/15ff680b-be1a-4399-b107-53f3fee2a76a" />
<br>
<br>
<img width="303" height="552" alt="Screenshot 2025-10-15 210342" src="https://github.com/user-attachments/assets/ee0aa57d-3c3e-4d10-87fb-0417e0dddfbc" />
<br>
## v)Image Rotation
<br>
<img width="293" height="524" alt="image" src="https://github.com/user-attachments/assets/6eeb01ea-0bd5-4c7a-af60-758a62885a81" />
<br>
## vi)Image Cropping
<br>
<img width="491" height="523" alt="image" src="https://github.com/user-attachments/assets/2e23f52f-3e71-43ca-a847-1bf2a73d3052" />
<br>
# Result: 

Thus the different image transformations such as Translation, Scaling, Shearing, Reflection, Rotation and Cropping are done using OpenCV and python programming.
