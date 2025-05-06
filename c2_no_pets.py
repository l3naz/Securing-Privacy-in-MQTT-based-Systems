import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"[C2] Received: {msg.payload.decode()}")

client = mqtt.Client()
client.connect("localhost")
client.subscribe("victim/sos")
client.on_message = on_message

print("C2 Subscriber (No PETs) - Waiting for messages...")
client.loop_forever()