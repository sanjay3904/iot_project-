# IoT Temperature Monitoring System

## Overview
This project consists of three main components:

1. **Publisher**: Reads data from a simulated temperature sensor and publishes it to an MQTT broker every 60 seconds.
2. **Subscriber**: Subscribes to the MQTT topic, processes incoming messages, saves data locally, and raises an alarm if the temperature exceeds a threshold continuously for 5 minutes.
3. **Server**: Exposes an HTTP endpoint that returns the last recorded temperature.

## Setup

### Publisher
1. Navigate to the `publisher` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the publisher: `python publisher.py`

### Subscriber
1. Navigate to the `subscriber` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the subscriber: `python subscriber.py`

### Server
1. Navigate to the `server` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python server.py`
4. Access the temperature data at `http://localhost:5000/temperature`

## Note
- Make sure the MQTT broker address in the code is correct.
- The subscriber stores data in an SQLite database named `temperature_data.db`.
