from config import *
import robot
import gripper
import conveyor
import vision
import socket, time


def main():
    # Main pick-and-place workflow: detect object -> move to pick -> close gripper -> lift -> notify vision
    # Connect to robot, gripper, conveyor belt, and vision system
    r = robot.connect()
    gripper.connect()
    conveyor.connect()
    vision.connect()

    # Start conveyor belt
    conveyor.start()

    # Open the gripper
    gripper.open()

    print("Waiting for object to be detected by vision system...")
    # Wait until vision system sends !FOUND! signal
    v_data = b''
    while v_data.decode('utf-8').strip() != '!FOUND!':
        v_data = vision.v.recv(20)
        print(f'Vision recv: {v_data.decode("utf-8").strip()}')
        if v_data == '!FOUND!':
            break
    print('OBJECT FOUND')

    v_data = vision.recv()
    print(v_data)
    
    # Extract x (mm), y (mm), rz (degrees) from vision system
    x, y, rz = v_data[0], v_data[1], v_data[2]

    # Move down to pick
    print('Moving down to pick...')
    robot.movej([(x/1000)-0.01, y/1000, 0.15, 2.222, 2.222, 0], speed=3, acc=3, blend=0, tool_rotation_deg=-rz)
    time.sleep(1.2)

    # Close the gripper
    gripper.close()

    # Lift up
    print('Lifting up...')
    # r.send(f'movel(p[0.093, -0.333, 0.344, 2.222, 2.222, 0], 2.0, 1.4, 2, 0)\n'.encode('utf-8'))
    robot.movel([0.093, -0.333, 0.344, 2.222, 2.222, 0], speed=2.5, acc=2.5)

    time.sleep(1)
    vision.send('!PICKED')

    # Stop conveyor belt
    conveyor.stop()


if __name__ == "__main__":
    main()