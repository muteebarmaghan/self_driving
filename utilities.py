import cv2
import numpy as np


minLineLength = 5
maxLineGap = 10
theta = 0
thetas = 0


def color_mask(image):
    return None


def roi(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, [vertices], 255)
    masked = cv2.bitwise_and(image, mask)
    return masked