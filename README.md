# Robotics Term Project: Dynamic Object Acquisition
**System:** Universal Robots UR3 + NI Vision Builder + Python

---

## Project Overview
The objective of this project is to implement an automated system where a **UR3 robotic arm** identifies, tracks, and captures a **moving box**. This requires real-time synchronization between a machine vision system and the robot's motion controller.

---

## Technical Workflow

### Phase 1: Vision & Perception
Using **NI Vision Builder**, the system performs image processing to extract data points:
* **Position:** Real-time $(X, Y)$ coordinates within the camera's Field of View (FOV).
* **Orientation:** The angular rotation ($\theta$) of the box to align the gripper.
* **Dimensions:** Size detection to ensure proper gripper stroke width.

### Phase 2: Data Processing & Control
A **Python** script of the operation, performing the following:
1.  **Data Ingestion:** Receiving vision data from NI Vision Builder via TCP/IP or Modbus.
2.  **Coordinate Mapping:** Transforming coordinates from the *Camera Frame* to the *Robot Base Frame*.
3.  **Trajectory Prediction:** Calculating the intercept point based on the velocity of the moving box.
4.  **Command Generation:** Sending URScript commands to the UR3 controller.

### Phase 3: Physical Execution
The **UR3 Robot** executes the motion profile:
* **Approach:** Moving the end-effector to the predicted path.
* **Grasp:** Actuating the gripper to secure the moving target.
* **Store:** Place the box outside the conveyer belt.

---

## System Architecture

| Component | Technology | Responsibility |
| :--- | :--- | :--- |
| **Vision** | NI Vision Builder 2023 Q3 | Feature extraction & geometry |
| **Logic** | Python 3.x | Control the robot and calculate neccessary variable |
| **Hardware** | UR3 Robot | Precision motion & physical grasping |
| **End-Effector** | Robotic Gripper | Object securement |

---
