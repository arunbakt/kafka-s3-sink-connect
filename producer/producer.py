import os
import json
from datetime import datetime
from kafka import KafkaProducer
import time

# Fetch Kafka brokers from environment variable
BROKER_LIST = os.getenv("KAFKA_BROKER_LIST", "localhost:9092,localhost:9093,localhost:9094")
TOPIC = os.getenv("KAFKA_TOPIC", "test-topic")

def get_minute_level_timestamp():
    """Returns current timestamp rounded to the nearest minute."""
    now = datetime.utcnow()
    return now.isoformat()+"Z"

def produce_messages():
    producer = KafkaProducer(
        bootstrap_servers=BROKER_LIST.split(","),
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )
    print(f"Producing messages to topic '{TOPIC}' on brokers '{BROKER_LIST}'...")

    while True:
        message = {
            "eventName": "testEvent",
            "payloadTimestamp": get_minute_level_timestamp(),
            "data": "Example JSON message",
        }
        producer.send(TOPIC, value=message)
        print(f"Sent: {message}")
        time.sleep(0.5)  # Send a message every 5 seconds

if __name__ == "__main__":
    produce_messages()