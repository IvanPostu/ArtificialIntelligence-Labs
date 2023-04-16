import cv2
import numpy as np
import matplotlib.pyplot as plt


def sharpen_function(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Define the sharpening kernel
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

    # Apply the kernel to the image
    sharpened = cv2.filter2D(img, -1, kernel)

    # Plot the original and sharpened images side by side
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[0].set_title("Original Image")
    axs[1].imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
    axs[1].set_title("Sharpened Image")

    plt.show()


# sharpen_function("/home/ivan/Desktop/ArtificialIntelligence/Lab4/q1.png")
