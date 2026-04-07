import socket, time
from config import *


def connect():
    # Connect to robot
    global r
    r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r.connect((ip_robot, port_rtde))
    print('Connected to robot')

    return r

def rotate_rz(rz):
    # Rotate robot around Z-axis
    r.send(b'movej(), 1.2, 0.4, 0, 0)\n')
    time.sleep(1)

if __name__ == "__main__":
    r = connect()
    r.send(b'movel(p[0.116, -0.300, 0.200, 0, -3.143, 0], 1.2, 0.4, 0, 0)\n')
    time.sleep(1)