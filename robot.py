import socket, time, math
from config import *

def connect():
    # Connect to robot
    global r
    r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r.connect((ip_robot, port_rtde))
    print('Connected to robot')

    return r

def movej(pose, tool_rotation_deg=0, speed=1.2, acc=0.4, blend=0):
    """
    pose: [x, y, z, rx, ry, rz] in meters and radians
    tool_rotation_deg: Clockwise/Counter-clockwise rotation of the tool in degrees
    """
    # Convert the desired tool rotation from degrees to radians
    rot_rad = math.radians(tool_rotation_deg)
    
    # p[0,0,0,0,0, rot_rad] applies a rotation ONLY around the Tool Z axis.
    cmd = (
        f"def my_move():\n"
        f"  target_pose = p[{pose[0]:.4f}, {pose[1]:.4f}, {pose[2]:.4f}, {pose[3]:.4f}, {pose[4]:.4f}, {pose[5]:.4f}]\n"
        f"  rotation = p[0, 0, 0, 0, 0, {rot_rad:.4f}]\n"
        f"  final_pose = pose_trans(target_pose, rotation)\n"
        f"  movej(final_pose, a={acc}, v={speed}, r={blend})\n"
        f"end\n"
    )
    
    r.send(cmd.encode())

def movel(pose, speed=1.2, acc=0.4, blend=0, wait=0):
    cmd = f'movel(p[{pose[0]:.3f}, {pose[1]:.3f}, {pose[2]:.3f}, {pose[3]:.3f}, {pose[4]:.3f}, {pose[5]:.3f}], {speed}, {acc}, {blend}, {wait})\n'
    r.send(cmd.encode())

if __name__ == "__main__":
    r = connect()
    
    # Move to home position (Tool facing down)
    base_pose = [0.116, -0.300, 0.200, 0, -3.143, 0]
    
    print("Moving to base pose...")
    movej(base_pose)
    time.sleep(3)