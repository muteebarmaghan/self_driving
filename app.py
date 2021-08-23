from flask import Flask, render_template, request, redirect, url_for, make_response
# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
import motors
import socket

motors.stop()

# Get server ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', server_ip=server_ip)


@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin)
    print(changePin)
    if changePin == 1:
        motors.left()
        print("Left")
    elif changePin == 2:
        motors.straight()
        print("farward")
    elif changePin == 3:
        motors.right()
        print("right")
    elif changePin == 4:
        motors.back()
        print("back")
    elif changePin == 5:
        motors.stop()
        print("stop")
    else:
        print("Wrong command")

    response = make_response(redirect(url_for('index')))
    return (response)


 # app.debug = True
 # app.run(host='0.0.0.0')
def connect():
 app.run(host='0.0.0.0', port=8000)
