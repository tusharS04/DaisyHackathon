import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


def cartoonify(image = None):
    input_file = Image.open(sys.argv[1])
    imgage = cv2.imread(input_file)
    imgage = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10,10))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    plt.figure(figsize=(10,10))
    plt.imshow(gray,cmap="gray")

    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    plt.figure(figsize=(10,10))
    plt.imshow(edges,cmap="gray")

    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    plt.figure(figsize=(10,10))
    plt.imshow(cartoon,cmap="gray")

    final = deepcopy(cartoon)
    final = 1 - final
    threshold = 0.1
    final[final > threshold] = 1
    final[final < threshold] = 0

    return final
