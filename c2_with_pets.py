import paho.mqtt.client as mqtt

# PET 3: XOR Decryption (Same key as publisher)
def xor_decrypt(message, key):
    return ''.join(chr(ord(c) ^ key) for c in message)

key = 42  # Must match publisher's key

def on_message(client, userdata, msg):
    encrypted_msg = msg.payload.decode()
    decrypted_msg = xor_decrypt(encrypted_msg, key)
    print(f"[C2] Decrypted: {decrypted_msg}")

client = mqtt.Client()
client.connect("localhost")
client.subscribe("victim/sos_secure")
client.on_message = on_message

print("C2 Subscriber (With PETs) - Waiting for encrypted messages...")
client.loop_forever()