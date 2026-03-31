import socket, time, sys
import math
from config import *

x, y, rz, d = [0,0,0,0]

def connect():
    # Connect to vision system
    global v
    global conn
    v = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    v.settimeout(10)
    try:
        v.bind((ip_vs, port_vs))
        v.listen(1)
        conn, addr = v.accept()
        print("Connected by", addr)
    except socket.timeout:
        print('Timeout: could not connect to vision system')
        sys.exit(1)
    except socket.error as e:
        print(f'Socket error: {e}')
        sys.exit(1)

    return v


def send(cmd):
    conn.send(str.encode(cmd + '\n'))
    time.sleep(0.1)


def recv():
    global x, y, rz, d
    # v_data = b''
    # while not v_data:
    #     v_data = v.recv(1024)
    #     time.sleep(0.1)
    # decoded = v_data.decode('utf-8').strip()
    # x, y, rz, d  = decoded.split(',')
    # print(f'Vision recv: x={x}, y={y}, rz={rz}, d={d}')
    # return float(x), float(y), float(rz), float(d)

    v_data = conn.recv(1024)
    if not v_data:
        return
    decoded = v_data.decode("utf-8", errors="ignore").strip().replace('\\n','\n')
    print(decoded)
    splitted = decoded.split(',')[-4:]  # get last 4 values, ignore any preceding text
    if len(splitted) == 4:
        x, y, rz, d  = splitted
        print(f'Vision recv: x={x}, y={y}, rz={rz}, d={d}')
    return float(x)/1000, float(y)/1000, math.radians(float(rz)), float(d)


if __name__ == "__main__":
    connect()
    # v.listen(1)
    print(recv())