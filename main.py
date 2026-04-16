from config import *
import robotv2
import gripper
import conveyor
import vision
import socket, time


def main():
    # Connect to robot, gripper, conveyor belt, and vision system
    r = robotv2.connect()
    gripper.connect()
    conveyor.connect()
    vision.connect()

    # Start conveyor belt
    conveyor.start()

    # Open the gripper
    gripper.open()

    # Move to Starting Position
    # print("Moving to starting position...")
    # r.send(b'movej(p[0.095, -0.296, 0.478, 2.222, 2.222, 0], 1.2, 0.4, 2, 0)\n')
    # time.sleep(2)  # Wait for the robot to move


    print("Waiting for object to be detected by vision system...")
    #wait until Recv(!FOUND) from vision system
    v_data = b''
    while v_data.decode('utf-8').strip() != '!FOUND!':
        v_data = vision.v.recv(20)
        # time.sleep(0.1)
        print(f'Vision recv: {v_data.decode("utf-8").strip()}')
        if v_data == '!FOUND!':
            break
    print('OBJECT FOUND')

    v_data = vision.recv()
    print(v_data)
    x, y, rz = v_data[0], v_data[1], v_data[2]

    # Move to the position above the conveyor belt
    print(f'Moving to position above object at x={x}, y={y}...')
    # r.send(f'movej(p[{x/1000}, {y/1000}, 0.300, 2.222, 2.222, 0], 2.0, 1.4, 0, 0)\n'.encode('utf-8'))
    # robotv2.movej([x/1000, y/1000, 0.300, 2.222, 2.222, 0], speed=2.5, acc=2.5, blend=0, tool_rotation_deg=-rz)
    # time.sleep(1)

    # Move down to pick
    print('Moving down to pick...')
    # r.send(f'movel(p[{(x/1000)-0.03}, {y/1000}, 0.15, 2.222, 2.222, 0], 1.2, 0.4, 0, 0)\n'.encode('utf-8'))
    robotv2.movej([(x/1000)-0.01, y/1000, 0.15, 2.222, 2.222, 0], speed=3, acc=3, blend=0, tool_rotation_deg=-rz)
    time.sleep(1.2)

    # Close the gripper
    gripper.close()

    # Lift up
    print('Lifting up...')
    # r.send(f'movel(p[0.093, -0.333, 0.344, 2.222, 2.222, 0], 2.0, 1.4, 2, 0)\n'.encode('utf-8'))
    robotv2.movel([0.093, -0.333, 0.344, 2.222, 2.222, 0], speed=2.5, acc=2.5)

    time.sleep(1)
    vision.send('!PICKED')

    # Stop conveyor belt
    conveyor.stop()


if __name__ == "__main__":
    main()