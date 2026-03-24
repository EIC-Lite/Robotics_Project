import socket, time
from config import *


def connect():
    # Connect to robot
    global r
    r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r.connect((ip_robot, port_rtde))
    print('Connected to robot')

    return r

