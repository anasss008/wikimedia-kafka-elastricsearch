from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

# Kafka configuration
KAFKA_BROKER = "kafka:9092"
KAFKA_TOPIC = "wikimedia-recentchange"

# Elasticsearch configuration
ELASTICSEARCH_HOST = "http://elasticsearch:9200"
ELASTICSEARCH_INDEX = "wikimedia"

def main():
    # Initialize Kafka Consumer
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda v: json.loads(v.decode("utf-8"))
    )

    # Initialize Elasticsearch client
    es = Elasticsearch([ELASTICSEARCH_HOST])

    # Consume and index data in Elasticsearch
    for message in consumer:
        try:
            document = message.value
            print(f"Indexing document in Elasticsearch: {document}")
            es.index(index=ELASTICSEARCH_INDEX, body=document)
        except Exception as e:
            print(f"Error indexing document: {e}")

if __name__ == "__main__":
    main()
