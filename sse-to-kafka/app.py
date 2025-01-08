import sseclient
import json
from kafka import KafkaProducer

# Kafka configuration
KAFKA_BROKER = "kafka:9092"  # Kafka broker address
KAFKA_TOPIC = "wikimedia-recentchange"

# Wikimedia SSE URL
WIKIMEDIA_SSE_URL = "https://stream.wikimedia.org/v2/stream/recentchange"

def main():
    # Initialize Kafka Producer
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    # Connect to SSE Stream
    print("Connecting to Wikimedia SSE stream...")
    client = sseclient.SSEClient(WIKIMEDIA_SSE_URL)

    # Stream and produce to Kafka
    for event in client:
        try:
            if event.data:
                data = json.loads(event.data)  # Parse event data as JSON
                print(f"Producing event to Kafka: {data}")
                producer.send(KAFKA_TOPIC, value=data)  # Send data to Kafka
        except Exception as e:
            print(f"Error processing event: {e}")

if __name__ == "__main__":
    main()
