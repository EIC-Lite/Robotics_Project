import socket

# Hardcoded for testing to rule out config.py errors
IP_VS = '10.10.1.10'
PORT_VS = 5000

def test_vision():
    # 1. Setup the socket
    v = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    v.settimeout(5) # 5 second timeout so it doesn't hang forever
    
    try:
        # 2. Connect
        print(f"Connecting to {IP_VS}:{PORT_VS}...")
        v.connect((IP_VS, PORT_VS))
        print("Connected successfully!")
        
        # 3. Send (Mimicking SocketTest's \r\n terminator)
        # Using ASCII encoding which is standard for industrial PLCs
        cmd = "cap!\r\n" 
        print(f"Sending: cap!")
        v.sendall(cmd.encode('ascii')) 
        
        # 4. Receive (Using a larger buffer of 1024 to catch everything)
        print("Waiting for response...")
        data = v.recv(1024)
        print(f"Raw bytes received: {data}")
        
        # 5. Parse
        if data:
            decoded = data.decode('ascii').strip()
            x, y, rz = decoded.split(',')
            print(f"Success! Parsed Vision Data: X={x}, Y={y}, Rz={rz}")
            
    except socket.timeout:
        print("Error: The connection timed out. The controller didn't respond.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Always close the socket cleanly
        v.close()
        print("Connection closed.")

if __name__ == "__main__":
    test_vision()