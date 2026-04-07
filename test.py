import socket, time, sys

ip_vs      = '127.0.0.1'   # Vision system IP address
port_vs    = 5555           # Vision system port

def connect():
    # Connect to vision system
    global v
    v = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    v.settimeout(10)
    try:
        v.connect((ip_vs, port_vs))
        print('Connected to vision system')
    except socket.timeout:
        print('Timeout: could not connect to vision system')
        sys.exit(1)
    except socket.error as e:
        print(f'Socket error: {e}')
        sys.exit(1)

    return v


def send(cmd):
    v.send(str.encode(cmd + '\n'))
    time.sleep(0.1)


def recv():
    v_data = b''
    while not v_data:
        v_data = v.recv(20)
        time.sleep(0.1)
    decoded = v_data.decode('utf-8').strip()
    x, y, rz = decoded.split(',')
    print(f'Vision recv: x={x}, y={y}, rz={rz}')
    return float(x), float(y), float(rz)   # returns (X, Y, Rz) in pixels/mm from camera

if __name__ == "__main__":
    v = connect()
    send('cap!')
