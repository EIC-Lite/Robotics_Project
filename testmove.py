from config import *
import robot
import time
import gripper
import math

def main():
    r = robot.connect()
    g = gripper.connect()

    # Open the gripper
    gripper.open()

    # Move to Starting Position
    r.send(b'movej(p[0.196, -0.335, 0.225, 2.222, 2.222, 0], 1.2, 0.4, 2, 0)\n')
    time.sleep(3)  # Wait for the robot to move

    r.send(b'movej(p[0.196, -0.335, 0.170, 2.222, 2.222, 0], 1.2, 0.4, 2, 0)\n')
    time.sleep(3)  # Wait for the robot to move

    # Close the gripper
    gripper.close()

    # Move back to the starting position
    r.send(b'movej(p[0.095, -0.296, 0.478, 2.222, 2.222, 0], 1.2, 0.4, 2, 0)\n')
    time.sleep(3)  # Wait for the robot to move


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