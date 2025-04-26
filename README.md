# Securing-Privacy-in-MQTT-based-Systems
Design and implement a privacy-enhanced MQTT-based messaging system for disaster scenarios involving victims, drones (brokers), and a Command &amp; Control (C2) system. Identify privacy threats using LINDDUN and apply Privacy-Enhancing Technologies (PETs).
  

## Setup  
1. Install Mosquitto: `sudo apt install mosquitto`  
2. Run `python c2_subscriber.py` (C2 server)  
3. Run `python victim_publisher.py` (victim client)  

## Privacy Enhancements  
- **Pseudonymization:** Victims use random IDs.  
- **Data Minimization:** Locations generalized to sectors.  
