import paho.mqtt.client as mqtt
import random

# PET 1: Pseudonymization
victim_id = random.randint(1000, 9999)  # Random ID instead of name

# PET 2: Data Minimization
def generalize_location(raw_location):
    sectors = ["A1", "A2", "B1", "B2", "C1", "C2"]
    return random.choice(sectors)  # Fake generalized location

# PET 3: XOR Encryption (Key must match subscriber)
def xor_encrypt(message, key):
    return ''.join(chr(ord(c) ^ key) for c in message)

broker = "localhost"
topic = "victim/sos_secure"
key = 42  # Simple XOR key (shared with C2)

client = mqtt.Client()
client.connect(broker)

print(f"Victim Publisher (With PETs) - Your ID: {victim_id}")
try:
    while True:
        raw_location = input("Your real location (e.g., 'Lat: 10, Long: 20'): ")
        generalized_loc = generalize_location(raw_location)
        plaintext_msg = f"{victim_id}:SOS:{generalized_loc}"
        encrypted_msg = xor_encrypt(plaintext_msg, key)
        client.publish(topic, encrypted_msg)
        print(f"Sent (encrypted): {encrypted_msg}")
except KeyboardInterrupt:
    client.disconnect()