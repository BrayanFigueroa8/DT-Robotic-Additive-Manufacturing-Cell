# DT-Robotic-Additive-Manufacturing-Cell
# Brayan S. Figueroa

This repository contains the components and files used to develop a Digital Twin (DT) for a robotic additive manufacturing cell. The project integrates various technologies such as MQTT, RoboDK, Node-RED, and Firestore to enable real-time data collection, simulation, and monitoring. Below is a description of each file and its role in the project.

## MQTT Publisher
The file `mqttPublisher.pscj` functions as an MQTT socket, installed directly on the robot controller. It acts as a publisher, continuously extracting real-time operational data from the robot and transmitting it over the MQTT protocol. To ensure proper functionality, this file must be installed in the following directory on the robot controller:  `C:\KRC\ROBOTER\Config\User\Common\OpcUa`. This file is responsible for ensuring the reliable and consistent flow of data from the robotic system to other components that rely on this data for monitoring and simulation purposes.

## RoboDK 3D Environment
The file `roboDK3D.rdk` is the 3D environment file for RoboDK, which contains the 3D model of the robotic additive manufacturing cell. Within RoboDK, there is a Python environment where the file `robodk_move.py` is used to subscribe to the MQTT data sent from the robot controller via Mosquitto, converting the data into the 3D simulation.

## Node-RED Flow
The file `nodered_flow.json` contains the Node-RED flow responsible for subscribing to the data via MQTT. This flow performs the data conversion, displays the dashboard graphics, and sends the data to the Firestore cloud storage.

## IDEF0 Diagrams and DT Methodology
The file `index.html` and the folder `IDEF0 DT Robotic Additive Manufacturing` contain the IDEF0 diagrams developed as the methodology for the creation and explanation of the Digital Twin (DT) of the robotic additive manufacturing cell. These diagrams can also be accessed at the following link: [IDEF0 DT Robotic Additive Manufacturing Cell](https://brayanfigueroa8.github.io/DT-Robotic-Additive-Manufacturing-Cell/).


