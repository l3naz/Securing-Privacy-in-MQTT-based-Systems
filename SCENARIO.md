# **Disaster Communication Scenario: MQTT Privacy Implementation**  
## **Scenario Overview**  
In a post-earthquake scenario, victims use drones (MQTT brokers) to send SOS messages to a Command & Control (C2) center. Attackers may intercept these messages to track victims or disrupt rescue efforts.  

### **Key Actors**  
| **Actor**       | **Role**                                  | **Privacy Risk**                  |  
|-----------------|------------------------------------------|-----------------------------------|  
| Victims         | Send SOS messages (e.g., location, name) | Identifiability, Linkability      |  
| Drones (Brokers)| Relay messages to C2                     | Detectability, Disclosure         |  
| C2 Center       | Coordinates rescue efforts               | Non-compliance, Unawareness       |  
| Attackers       | Eavesdrop on MQTT traffic                | Disclosure, Non-repudiation

## **Simulating the Scenario**  
### **Environment Setup**   
#### Baseline No PETs 
1. Start the subscriber (C2):  
   ```bash
   python3 baseline/c2_no_pets.py
   ```
2. Run the publisher (Victim):  
   ```bash
   python3 baseline/victim_no_pets.py
   ```

#### Privacy-Enhanced (With PETs)  
1. Start the subscriber (C2):  
   ```bash
   python3 enhanced/c2_with_pets.py
   ```
2. Run the publisher (Victim):  
   ```bash
   python3 enhanced/victim_with_pets.py
   ```
## **Interpreting Results**  
### **1. Message Structure Comparison**  
| **System**       | **Example Message**                          | **Privacy Level** |  
|------------------|---------------------------------------------|------------------|  
| Baseline         | `"John Doe: SOS at Lat: 34.05, Long: -118.25"` | ❌ High risk      |  
| Enhanced         | `"#3847:SOS:Sector B2"` (XOR-encrypted)       | ✅ Medium risk    |  

### **2. Attack Simulation**  
- **Eavesdropping**:  
  - Run `mosquitto_sub -t "victim/#" -v` to spy on topics.  
  - **Baseline**: Attackers see exact locations.  
  - **Enhanced**: Attackers see encrypted gibberish (e.g., `"�\x12�\x0f��\x1d"`).  

### **3. Key Takeaways**  
- **Without PETs**: Victims’ identities/locations are fully exposed.  
- **With PETs**:  
  - Pseudonyms protect identities.  
  - Generalized locations reduce precision.  
  - XOR encryption obscures payloads (but is not production-ready).

### Results
- Results with no PETs implemented:
![image](https://github.com/user-attachments/assets/d998e5c2-fe1f-4857-9f4a-5c58cc3e4560)

- Results with PETs implemented:
![image](https://github.com/user-attachments/assets/f8b901ed-03fe-490e-8703-e2aa5da4e474)

