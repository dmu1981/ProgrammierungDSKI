import cv2
import os


for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if name.endswith(".png"):
            img = cv2.imread(name, cv2.IMREAD_UNCHANGED)
            img = cv2.resize(img, (100, 100))
            cv2.imwrite("100x100_" + name, img)
