import cv2
import csv


def is_colored(image):
    height, width, channels = image.shape

    for y in range(height):
        for x in range(width):
            pixel = image[y, x]
            if not all(pixel == pixel[0]):
                return True

    return False


def is_portrait(image):
    height, width, channels = image.shape

    if height >= width:
        return True
    return False


def is_eyes_at_same_level(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(eyes) != 2:
        return False

    y1 = eyes[0][1] + eyes[0][3] // 2
    y2 = eyes[1][1] + eyes[1][3] // 2

    diff = abs(y1 - y2)

    if diff <= 5:
        return True

    return False


def contains_only_one_person(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    if len(faces) == 1:
        return True

    return False


def head_area_percentage(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    if len(faces) == 0:
        return None
    (x, y, w, h) = faces[0]
    top_of_head = y - int(h * 0.25)
    head_area = w * int(h * 0.75)
    image_area = image.shape[0] * image.shape[1]
    head_area_percentage = (head_area / image_area) * 100
    return head_area_percentage


def is_accepted_for_passport(img_path):
    image = cv2.imread(img_path)
    return all(
        [
            is_colored(image),
            is_portrait(image),
            is_eyes_at_same_level(image),
            contains_only_one_person(image),
            head_area_percentage(image),
        ]
    )


with open(
    "/home/ivan/Desktop/ArtificialIntelligence/Lab4/test.csv", newline=""
) as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')
    passed = 0
    total = 0
    for row in reader:
        if row[0] == "new_path":
            continue

        total += 1
        img_path = "/home/ivan/Desktop/ArtificialIntelligence/Lab4/" + row[0]
        expected_value_for_is_accepted_for_passport = bool(row[1])
        current_value_for_is_accepted_for_passport = is_accepted_for_passport(img_path)
        if current_value_for_is_accepted_for_passport:
            passed += 1
        print(
            row[0],
            expected_value_for_is_accepted_for_passport,
            current_value_for_is_accepted_for_passport,
        )
    print(f"Accuracy: {passed / total * 100}")
