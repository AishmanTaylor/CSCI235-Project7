#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import socket
import lib

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

# 172.17.3.91 Previous IP 
SERVER_IP = "172.17.9.195"
PORT = 8888

def send_message(message):
    reply = None
    try:
        sock = socket.socket()
        sock.connect((SERVER_IP, PORT))
        sock.send(message.encode())
        reply = sock.recv(1024).decode()
    except Exception as e:
        reply = str(e)
    finally:
        sock.close()
    return reply

robot = lib.SensorMotor(ev3)
send_message("knn 3 avoid")
while True:
    msg = send_message("classify")
    if msg == "Label_A_Far":
        lib.go_forward(robot)
    elif msg == "Label_A_Close":
        lib.turn_left(robot)
    elif msg == "Label_B_Far":
        lib.go_forward(robot)
    elif msg == "Label_B_Close":
        lib.turn_left(robot)
    elif msg == "Label_C_Far":
        lib.go_forward(robot)
    elif msg == "Label_C_Close":
        lib.turn_left(robot)
    elif msg ==  "Label_Clear":
        lib.turn_left(robot)
    ev3.screen.clear()
    ev3.screen.draw_text(0, 0, msg)
