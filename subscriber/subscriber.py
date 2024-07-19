import time
import sqlite3
import paho.mqtt.client as mqtt

BROKER = 'mqtt.eclipse.org'
TOPIC = 'hotel/temperature'
CLIENT_ID = 'temperature_subscriber'
DATABASE = 'temperature_data.db'
THRESHOLD = 25.0
ALARM_DURATION = 5 * 60  # 5 minutes

def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode())
    timestamp = int(time.time())
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO temperature_data (timestamp, temperature) VALUES (?, ?)", (timestamp, temperature))
    conn.commit()
    
    cursor.execute("SELECT timestamp FROM temperature_data WHERE temperature > ?", (THRESHOLD,))
    rows = cursor.fetchall()
    if len(rows) >= 5:
        if rows[-1][0] - rows[-5][0] <= ALARM_DURATION:
            print("Alarm: Temperature threshold exceeded!")
    
    conn.close()

def main():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS temperature_data (timestamp INTEGER, temperature REAL)")
    conn.commit()
    conn.close()

    client = mqtt.Client(CLIENT_ID)
    client.connect(BROKER)
    client.on_message = on_message
    client.subscribe(TOPIC)
    client.loop_forever()

if __name__ == '__main__':
    main()

