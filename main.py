from config import *
import robot
import gripper
import conveyor
import vision
import socket, time


def main():
    # Connect to robot, gripper, conveyor belt, and vision system
    r = robot.connect()
    g = gripper.connect()
    conv = conveyor.connect()
    vs = vision.connect()

    # Start conveyor belt
    conveyor.start()

    # Open the gripper
    gripper.open()

    # Move to Starting Position
    r.send(b'movel(p[0.116, -0.300, 0.200, 0, -3.143, 0], 1.2, 0.4, 0, 0)\n')
    time.sleep(1)  # Wait for the robot to move

    # Move to the position above the conveyor belt
    r.send(b'movel(p[0.095, -0.296, 0.478, 2.222, 2.222, 0], 1.2, 0.4, 0, 0)\n')
    time.sleep(1)

    # Open the gripper
    gripper.open()

    # Trigger camera and get object offset (X, Y, Rz)
    vs.send('cap!')
    diffX, diffY, diffRz = vs.recv()

    # Move above the object
    # X, Y, RZ
    time.sleep(1)

    # Move down to pick
    # -Z
    time.sleep(1)

    # Close the gripper
    gripper.close()

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
    gripper.open()

    # Stop conveyor belt
    conveyor.stop()


if __name__ == "__main__":
    main()