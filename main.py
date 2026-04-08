from config import *
import robot
import gripper
import conveyor
import vision
import socket, time


def main():
    # Connect to robot, gripper, conveyor belt, and vision system
    r = robot.connect()
    gripper.connect()
    conveyor.connect()
    vision.connect()

    # Start conveyor belt
    conveyor.start()

    # Open the gripper
    gripper.open()

    # Move to Starting Position
    r.send(b'movel(p[0.116, -0.300, 0.200, 0, -3.143, 0], 1.2, 0.4, 0, 0)\n')
    time.sleep(1)  # Wait for the robot to move

    # #wait until Recv(!FOUND) from vision system
    while True:
        vision.send('cap!')
        v_data = b''
        while v_data.decode('utf-8').strip() != '!FOUND':
            v_data = vision.v.recv(20)
            time.sleep(0.1)
            print(f'Vision recv: {v_data.decode('utf-8').strip()}')
        print('OBJECT FOUND')
        break

    v_data = vision.recv()
    print(v_data)
    x, y, rz = v_data[0], v_data[1], v_data[2]

    # Move to the position above the conveyor belt
    r.send(f'movel(p[{x}, {y}, 0.478, 2.222, 2.222, 0], 1.2, 0.4, 0, 0)\n'.encode('utf-8')) # Have to offset x and calibrate z
    time.sleep(1)

    # Move down to pick
    r.send(f'movel(p[{x}, {y}, 0.1, 2.222, 2.222, 0], 1.2, 0.4, 0, 0)\n'.encode('utf-8'))
    time.sleep(1)

    # Close the gripper
    gripper.close()

    # Lift up
    r.send(f'movel(p[{x}, {y}, 0.478, 2.222, 2.222, 0], 1.2, 0.4, 0, 0)\n'.encode('utf-8'))
    time.sleep(1)
    vision.send('!PICKED')

    # Stop conveyor belt
    conveyor.stop()


if __name__ == "__main__":
    main()