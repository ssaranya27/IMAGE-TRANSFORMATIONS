 # Vertical shear
shear_matrix_y = np.float32([[1, 0, 0], [0.5, 1, 0]])
sheared_y = cv2.warpAffine(image, shear_matrix_y, (w, int(h + 0.5*w)))


    # --------------------- 5. Rotation ---------------------
    angle = 45
    scale_factor = 1.0
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale_factor)
    rotated = cv2.warpAffine(image, rotation_matrix, (w, h))


    # --------------------- 6. Cropping ---------------------
    cropped = image[0:200, 0:200]  # Crop top-left 200x200 region

    # --------------------- 7. Display All Results ---------------------
    images = [image, translated, scaled, sheared_x, sheared_y, h_flip, v_flip, rotated, cropped]
    titles = ["Original", "Translated", "Scaled", "Sheared X", "Sheared Y",
              "Horizontally Flipped", "Vertically Flipped", "Rotated", "Cropped"]

    plt.figure(figsize=(20, 10))
    for i in range(len(images)):
        plt.subplot(3, 3, i+1)
        show_image(images[i], titles[i])
    plt.tight_layout()
    plt.show()

