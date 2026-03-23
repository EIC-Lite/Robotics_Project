from config import *
from robot import *
from gripper import *
from conveyor import *
from vision import *


def main():
    # Connect to robot, gripper, conveyor belt, and vision system
    r = robot_connect()
    g = gripper_connect()
    conv = conveyor_connect()
    vs = vision_connect()

    # Start conveyor belt
    conveyor_start()

    # Open the gripper
    gripper_open()

    # Move to Starting Position
    r.send(b'movel(p[0.116, -0.300, 0.200, 0, -3.143, 0], 1.2, 0.4, 0, 0)\n')
    time.sleep(2)  # Wait for the robot to move

    # Move to the position above the conveyor belt
    #
    #

    # Open the gripper
    gripper_open()

    # Trigger camera and get object offset (X, Y, Rz)
    vs_send('cap!')
    diffX, diffY, diffRz = vs_recv()

    # Move above the object
    # X, Y, RZ
    time.sleep(1)

    # Move down to pick
    # -Z
    time.sleep(1)

    # Close the gripper
    gripper_close()

    # Lift up
    # +Z
    time.sleep(1)

    # Move to place position
    # X, Y, RZ
    time.sleep(1)

    # Move down to place
    # -Z
    time.sleep(1)

    # Open the gripper
    gripper_open()

    # Stop conveyor belt
    conveyor_stop()


if __name__ == "__main__":
    main()