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
    # Rotate robot around Z-axis
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

def movej(pose, speed=1.2, acc=0.4, blend=0, wait=0):
    cmd = f'movej(p[{pose[0]:.3f}, {pose[1]:.3f}, {pose[2]:.3f}, {pose[3]:.3f}, {pose[4]:.3f}, {pose[5]:.3f}], {speed}, {acc}, {blend}, {wait})\n'
    r.send(cmd.encode())
    time.sleep(1)

    
if __name__ == "__main__":
    r = connect()
    movej([0.116, -0.300, 0.200, 0, -3.143, 0], speed=1.2, acc=0.4, blend=0, wait=0)
    time.sleep(1)
    rotate_rz(90)
    time.sleep(1)