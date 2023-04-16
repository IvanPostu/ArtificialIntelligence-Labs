import matplotlib

matplotlib.use("TkAgg")

import cv2
import matplotlib.pyplot as plt


def detect_face(image):
    # Load the pre-trained Haar cascades classifier for face detection
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization to improve contrast
    equalized_image = cv2.equalizeHist(gray_image)

    # Detect faces in the image using the Haar cascades classifier
    faces = face_cascade.detectMultiScale(
        equalized_image, scaleFactor=1.3, minNeighbors=5
    )

    # If no faces are detected, return None
    if len(faces) == 0:
        return None
    else:
        face = max(faces, key=lambda x: x[2] * x[3])
        x, y, w, h = face
        return (x, y, x + w, y + h)


image = cv2.imread("/home/ivan/Desktop/ArtificialIntelligence/Lab4/person1.png")

face_coords = detect_face(image)

# If a face is detected, draw a rectangle around it
if face_coords is not None:
    x1, y1, x2, y2 = face_coords
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
