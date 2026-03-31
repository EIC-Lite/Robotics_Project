from config import *
import robot
import time
import vision
import math

def main():
    r = robot.connect()
    vs = vision.connect()

    # Move to Starting Position
    r.send(b'movej(p[0.095, -0.296, 0.478, 2.222, 2.222, 0], 1.2, 0.4, 0, 0)\n')
    time.sleep(1)  # Wait for the robot to move

    # r.send(b'movej(p[0.167, -0.324, 0.240, 2.222, 2.222, 0], 1.2, 0.4, 0, 0)\n')
    # time.sleep(5)  # Wait for the robot to move

    # r.send(b'movej(p[0.095, -0.296, 0.478, 2.222, 2.222, 0], 1.2, 0.4, 0, 0)\n')
    # time.sleep(1)  # Wait for the robot to move

    # # vs.send(b'cap!')
    # x,y,rz,d = vision.recv()
    # print(f"Received from vision: x={x}, y={y}, rz={rz}, d={d}")
    # r.send(f'movel(p[{x}, {y}, 0.478, 2.222, 2.222, 0], 1.2, 0.4, 0, 0)\n'.encode('utf-8'))
    # r.send(f'movel(pose_add(get_actual_tcp_pose(),p[0, 0, 0, {rz}, 0, 0]))\n'.encode('utf-8'))


   





if __name__ == "__main__":
    main()