import socket, time
from config import *


def connect():
    # Connect to gripper
    global g
    g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    g.connect((ip_robot, port_g))
    g.send(b'GET ACT\n')

    # Activate the gripper
    g_recv = str(g.recv(10), 'UTF-8')
    print('GET ACT = ' + g_recv)
    g.send(b'GET POS\n')
    g_recv = str(g.recv(10), 'UTF-8')
    if g_recv:
        g.send(b'SET ACT 1\n')
        g_recv = str(g.recv(255), 'UTF-8')
        time.sleep(3)
        g.send(b'SET GTO 1\n')
        g.send(b'SET SPE 255\n')
        g.send(b'SET FOR 0\n')
    print('Gripper ready')


def open():
    # Open the gripper
    g.send(b'SET POS 0\n')
    g.recv(255)
    time.sleep(1)


def close():
    # Close the gripper
    g.send(b'SET POS 255\n')
    g.recv(255)
    time.sleep(1)


if __name__ == "__main__":
    g = connect()
    open()
    time.sleep(2)
    close()