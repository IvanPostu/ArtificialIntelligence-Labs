import matplotlib
matplotlib.use('TkAgg')

import cv2
import matplotlib.pyplot as plt


def blur_function(image_path, kernel_size=(5,5)):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply the Gaussian blur
    blurred = cv2.GaussianBlur(gray, kernel_size, 0)

    # Plot the original and blurred images side by side
    fig, axs = plt.subplots(1, 2, figsize=(10,5))
    axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Original Image')
    axs[1].imshow(blurred, cmap='gray')
    axs[1].set_title('Blurred Image')

    plt.show()

blur_function("/home/ivan/Desktop/ArtificialIntelligence/Lab4/q1.png")