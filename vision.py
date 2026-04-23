import socket, time, sys
from config import *


def connect():
    # Connect to vision system
    global v
    v = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        v.connect((ip_vs, port_vs))
        print('Connected to vision system')
    except socket.timeout:
        # Connection attempt exceeded timeout duration
        print('Timeout: could not connect to vision system')
        sys.exit(1)
    except socket.error as e:
        # Connection failed due to network error
        print(f'Socket error: {e}')
        sys.exit(1)

    return v


def send(cmd):
    # Send command to vision system with carriage return line feed delimiters
    global v
    print(f'Sending to vision: {cmd}')
    v.send(str.encode(cmd + '\r\n'))
    time.sleep(0.1)


def recv():
    # Receive and parse vision system response (format: x,y,rz)
    v_data = b''
    while not v_data:
        v_data = v.recv(20)
        time.sleep(0.1)
    decoded = v_data.decode('utf-8').strip()
    x, y, rz = decoded.split(',')  # Parse comma-separated values
    print(f'Vision recv: x={x}, y={y}, rz={rz}')
    return float(x), float(y), float(rz)  # Returns (X, Y, Rz) in pixels/mm from camera


if __name__ == "__main__":
    connect()
    send('cap!')
    print(recv())