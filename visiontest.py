import socket, time, sys
from config import *

x, y, rz, d = [0, 0, 0, 0]
v = None  # single connection socket

def connect():
    global v
    v = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    v.settimeout(10)
    try:
        v.connect((ip_vs, port_vs))  # Python is the CLIENT
        print(f"Connected to {ip_vs}:{port_vs}")
    except socket.timeout:
        print('Timeout: could not connect to vision system')
        sys.exit(1)
    except socket.error as e:
        print(f'Socket error: {e}')
        sys.exit(1)
    return v


def send(cmd):
    v.sendall((cmd + '\n').encode('utf-8'))
    time.sleep(0.1)


def recv():
    global x, y, rz, d
    v_data = v.recv(1024)
    if not v_data:
        return None
    decoded = v_data.decode('utf-8', errors='ignore').strip().replace('\\n', '\n')
    print(f'Raw: {decoded}')
    splitted = decoded.split(',')[-4:-1]  # get last 4 values, ignore any preceding text
    if len(splitted) == 4:
        x, y, rz, d = splitted  # use splitted, not decoded.split again
        print(f'Vision recv: x={x}, y={y}, rz={rz}, d={d}')
        return float(x), float(y), float(rz), float(d)
    else:
        print(f'Unexpected format: {splitted}')
        return None


if __name__ == "__main__":
    connect()
    send('cap!')       # trigger Vision Builder acquisition
    print(recv())