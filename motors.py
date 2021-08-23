import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Ena1, In1, In2, Ena2, In3, In4, = 2, 3, 4, 17, 27, 22
# In1, In2, In3, In4, = 3, 4,  27, 22
GPIO.setup(Ena1, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)
GPIO.setup(Ena2, GPIO.OUT)
GPIO.setup(In3, GPIO.OUT)
GPIO.setup(In4, GPIO.OUT)
pwm1 = GPIO.PWM(Ena1, 100)
pwm1.start(0)
pwm2 = GPIO.PWM(Ena2, 100)
pwm2.start(0)

def right():
    print("right")
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)
    GPIO.output(In3, GPIO.LOW)
    GPIO.output(In4, GPIO.HIGH)
def left():
    print("left")
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    GPIO.output(In3, GPIO.HIGH)
    GPIO.output(In4, GPIO.LOW)
def straight():
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)
    GPIO.output(In3, GPIO.HIGH)
    GPIO.output(In4, GPIO.LOW)
def stop():
    pwm1.ChangeDutyCycle(30)
    pwm2.ChangeDutyCycle(30)
    pwm1.ChangeDutyCycle(10)
    pwm2.ChangeDutyCycle(10)
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.LOW)
    GPIO.output(In3, GPIO.LOW)
    GPIO.output(In4, GPIO.LOW)
def back():
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    GPIO.output(In3, GPIO.LOW)
    GPIO.output(In4, GPIO.HIGH)
