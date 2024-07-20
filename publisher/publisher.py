import time
import random
import paho.mqtt.client as mqtt

BROKER = 'mqtt.eclipse.org' 
TOPIC = 'hotel/temperature'
CLIENT_ID = 'temperature_publisher'

def read_temperature():
    # Simulate reading temperature from a sensor
    return random.uniform(20.0, 30.0)

def main():
    client = mqtt.Client(CLIENT_ID)
    client.connect(BROKER)

    while True:
        temperature = read_temperature()
        payload = f"{temperature:.2f}"
        client.publish(TOPIC, payload)
        print(f"Published: {payload}")
        time.sleep(60)

if __name__ == '__main__':
    main()

