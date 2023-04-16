import matplotlib

matplotlib.use("TkAgg")

import cv2
import matplotlib.pyplot as plt
import numpy as np

#t1.py
def blur_function(image_path, kernel_size=(5,5)):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, kernel_size, 0)
    fig, axs = plt.subplots(1, 2, figsize=(10,5))
    axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Original Image')
    axs[1].imshow(blurred, cmap='gray')
    axs[1].set_title('Blurred Image')

    plt.show()

def sharpen_function(image_path):
    img = cv2.imread(image_path)
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(img, -1, kernel)
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[0].set_title("Original Image")
    axs[1].imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
    axs[1].set_title("Sharpened Image")
    plt.show()


blur_function("/home/ivan/Desktop/ArtificialIntelligence/Lab4/q1.png")
sharpen_function("/home/ivan/Desktop/ArtificialIntelligence/Lab4/q1.png")
