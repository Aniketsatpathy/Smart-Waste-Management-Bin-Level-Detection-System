import json
import os
import sys

# Add project root to sys.path to allow running this script directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# pyrefly: ignore [missing-import]
import paho.mqtt.client as mqtt

from backend.config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

from backend.database_manager import DatabaseManager

db = DatabaseManager()


def on_connect(client, userdata, flags, rc):

    print(f"Connected: {rc}")

    client.subscribe(MQTT_TOPIC)

    print(f"Subscribed to: {MQTT_TOPIC}")


def on_message(client, userdata, msg):

    try:

        payload = json.loads(msg.payload.decode())

        print("\nReceived:")

        print(payload)

        db.insert_reading(
            payload["bin_id"],
            payload["distance"],
            payload["fill_percentage"],
            payload["status"],
            payload["alert"],
        )

        print("Saved to SQLite")

    except Exception as e:

        print(f"Error: {e}")


client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)

client.loop_forever()
