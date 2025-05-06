import paho.mqtt.client as mqtt

broker = "localhost"  # Change if broker is remote
topic = "victim/sos"

client = mqtt.Client()
client.connect(broker)

print("Victim Publisher (No PETs) - Press Ctrl+C to exit")
try:
    while True:
        name = input("Your name: ")
        location = input("Your exact location (e.g., 'Lat: 10, Long: 20'): ")
        message = f"{name} needs help at {location}"
        client.publish(topic, message)
        print(f"Sent: {message}")
except KeyboardInterrupt:
    client.disconnect()