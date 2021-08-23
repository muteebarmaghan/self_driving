import cv2
import numpy as np
import math
from utilities import roi

minLineLength = 5
maxLineGap = 10
thetaa=0
# global thetas
thetas =0

def preprocessings(img):

    thetas = 0
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 85, 85)
    cv2.imshow("edges", edged)
    vertices = np.array([[10, 480], [213, 0], [426, 0], [630, 480]])
    roii = roi(edged, vertices)
    lines = cv2.HoughLinesP(roii, 1, np.pi / 180, 10, minLineLength, maxLineGap)

    if lines is not None:
        for x in range(0, len(lines)):
            for x1, y1, x2, y2 in lines[x]:
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                thetas = thetas + math.atan2((y2 - y1), (x2 - x1))
    return thetas
