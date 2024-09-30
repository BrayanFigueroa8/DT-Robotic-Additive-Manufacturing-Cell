# Brayan Stiven Figueroa Betancourth
# 3D movement simulation module AM KUKA-Meltio in RoboDK

from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox
from ast import literal_eval

from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox

import paho.mqtt.subscribe as subscribe

import json
import os
import re
import sys
sys.path.insert(0, 'path')
import ArcStart as ArcStart
import ArcEnd as ArcEnd
import numpy as np
from scipy.spatial.transform import Rotation

RDK = Robolink()

# Define the function to set joint angular speeds
def set_joint_speeds(angular_speeds):
    for i, speed in enumerate(angular_speeds):
        robot.setSpeed(i+1, speed)

# Define the function to move the robot to a specific position
def move_robot_to_position(joint_values):
    # Move the robot to the specified position
    robot.MoveJ(joint_values)

# Identify the robot and the table in the RoboDK simulation environment
robot = RDK.ItemUserPick('Select a robot', robolink.ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception('No robot selected or available')

table = RDK.Item('table')
print_reference = RDK.Item('print Reference')

# Define the function that will handle MQTT message reception
def on_CRobT(client, userdata, msg):
    # Decode the JSON message
    data = json.loads(msg.payload.decode())

    # Check the topic name
    if msg.topic == "Joints_Position":
        # Extract joint values
        val_a1 = data["Messages"][0]["Payload"]["PositionA1"]["Value"]
        val_a2 = data["Messages"][0]["Payload"]["PositionA2"]["Value"]
        val_a3 = data["Messages"][0]["Payload"]["PositionA3"]["Value"]
        val_a4 = data["Messages"][0]["Payload"]["PositionA4"]["Value"]
        val_a5 = data["Messages"][0]["Payload"]["PositionA5"]["Value"]
        val_a6 = data["Messages"][0]["Payload"]["PositionA6"]["Value"]

        # Convert values of a1, a4, and a6 to negatives
        val_a1 = -val_a1
        val_a4 = -val_a4
        val_a6 = -val_a6
        
        # Create an array with joint values
        joint_values = [val_a1, val_a2, val_a3, val_a4, val_a5, val_a6]

        # Print joint values in a single array
        print("Joint values:", joint_values)
        
        # Move the robot to the specified position
        move_robot_to_position(joint_values)
    
    elif msg.topic == "Joints_Speed":
        # Extract joint speed values
        vel_a1 = data["Messages"][0]["Payload"]["SpeedA1"]["Value"]
        vel_a2 = data["Messages"][0]["Payload"]["SpeedA2"]["Value"]
        vel_a3 = data["Messages"][0]["Payload"]["SpeedA3"]["Value"]
        vel_a4 = data["Messages"][0]["Payload"]["SpeedA4"]["Value"]
        vel_a5 = data["Messages"][0]["Payload"]["SpeedA5"]["Value"]
        vel_a6 = data["Messages"][0]["Payload"]["SpeedA6"]["Value"]

        # Define the radius of each joint (adjust these values according to your robot)
        r_joint1 = 100  # Suppose joint 1 radius is 100 mm
        r_joint2 = 100  # Suppose joint 2 radius is 100 mm
        r_joint3 = 100  # Suppose joint 3 radius is 100 mm
        r_joint4 = 100  # Suppose joint 4 radius is 100 mm
        r_joint5 = 100  # Suppose joint 5 radius is 100 mm
        r_joint6 = 100  # Suppose joint 6 radius is 100 mm

        # Calculate required angular speeds for each joint in radians per second
        ang_speed_joint1 = vel_a1 / r_joint1
        ang_speed_joint2 = vel_a2 / r_joint2
        ang_speed_joint3 = vel_a3 / r_joint3
        ang_speed_joint4 = vel_a4 / r_joint4
        ang_speed_joint5 = vel_a5 / r_joint5
        ang_speed_joint6 = vel_a6 / r_joint6

        # Create an array with joint angular speeds
        angular_speeds = [ang_speed_joint1, ang_speed_joint2, ang_speed_joint3,
                          ang_speed_joint4, ang_speed_joint5, ang_speed_joint6]

        # Print joint speed values in a single array
        print("Joint angular speeds:", angular_speeds)

        # Set angular speeds for the joints
        set_joint_speeds(angular_speeds)

# Subscribe to necessary topics for motion simulation
MY_TOPICS = [("Joints_Position", 0), ("Joints_Speed", 0)]
subscribe.callback(on_CRobT, MY_TOPICS, hostname="000.00.00.000", port=0000)