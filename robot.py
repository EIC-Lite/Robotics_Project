import socket, time, math
from config import *


def connect():
    # Connect to robot
    global r
    r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r.connect((ip_robot, port_rtde))
    print('Connected to robot')

    return r


def rotate_rz(RZ):
    # Rotate Rz
    rz = math.radians(RZ)
    cmd = (
        f'movej(['
        f'get_actual_joint_positions()[0], '
        f'get_actual_joint_positions()[1], '
        f'get_actual_joint_positions()[2], '
        f'get_actual_joint_positions()[3], '
        f'get_actual_joint_positions()[4], '
        f'get_actual_joint_positions()[5] + {rz:.6f}'
        f'], 1.2, 0.4, 0, 0)\n'
    )    
    r.send(cmd.encode())    
    time.sleep(1)

