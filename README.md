# MQTT Privacy-Enhanced Disaster Communication System  
*A project implementing Privacy-Enhancing Technologies (PETs) for secure messaging in calamity scenarios.*  

##  Overview  
This project simulates an MQTT-based communication system between victims and a Command & Control (C2) center during disasters. It demonstrates:  
- **Baseline (Insecure) Implementation**: Plaintext messaging with no privacy protections.  
- **Privacy-Enhanced Implementation**: Pseudonymization, data minimization, and encryption using XOR.  

##  Tools Used  
- **MQTT Broker**: [Mosquitto](https://mosquitto.org/)  
- **Python Libraries**: `paho-mqtt`  
- **Privacy Framework**: LINDDUN  

##  Setup Instructions  
### Prerequisites  
1. Install Mosquitto:  
   ```bash
   sudo apt-get install mosquitto mosquitto-clients  # Linux
   brew install mosquitto                            # macOS
   ```
2. Install Python dependencies:  
   ```bash
   pip install paho-mqtt
   ```
