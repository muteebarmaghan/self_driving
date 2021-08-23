from picamera.array import PiRGBArray
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import cv2
from preprocessings import preprocessings
import motors

##############################
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# Ena1, In1, In2, Ena2, In3, In4, = 2, 3, 4, 17, 27, 22
# # In1, In2, In3, In4, = 3, 4,  27, 22
# GPIO.setup(Ena1, GPIO.OUT)
# GPIO.setup(In1, GPIO.OUT)
# GPIO.setup(In2, GPIO.OUT)
# GPIO.setup(Ena2, GPIO.OUT)
# GPIO.setup(In3, GPIO.OUT)
# GPIO.setup(In4, GPIO.OUT)
# pwm1 = GPIO.PWM(Ena1, 100)
# pwm1.start(0)
# pwm2 = GPIO.PWM(Ena2, 100)
# pwm2.start(0)
###############################
minLineLength = 5
maxLineGap = 10
theta = 0
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
main_case = 0


def angle_theta():
    global image
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        theta = preprocessings(image)
        print(theta)

        threshold = 6
        if (theta > threshold):
            print("left")
            motors.left()
        if (theta < -threshold):
            print("right")
            motors.right()
        if (abs(theta) < threshold):
            motors.straight()
            print("straight")
        theta = 0
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        if key == ord("q"):
            break
    return image


# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# edged = cv2.Canny(blurred, 85, 85)
# # cv2.imshow("edges",edged)
# vertices = np.array([[10, 480], [213, 0], [426, 0], [630, 480]])
# roi = utilities.roi(edged, vertices)
# lines = cv2.HoughLinesP(roi, 1, np.pi / 180, 10, minLineLength, maxLineGap)

# if lines is not None:
#     for x in range(0, len(lines)):
#         for x1, y1, x2, y2 in lines[x]:
#             cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             theta = theta + math.atan2((y2 - y1), (x2 - x1))
# print(theta)
