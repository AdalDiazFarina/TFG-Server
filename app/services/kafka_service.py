from kafka import KafkaProducer, KafkaConsumer
import os
from dotenv import load_dotenv
import json

load_dotenv()
BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS")

class KafkaService:
    def __init__(self, bootstrap_servers=BOOTSTRAP_SERVERS):
        self.bootstrap_servers = bootstrap_servers

    def send(self, topic, message):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)
        producer.send(topic, json.dumps(message).encode('utf-8'))
        producer.flush()

    def receive(self, topic):
        consumer = KafkaConsumer(topic, bootstrap_servers=self.bootstrap_servers)
        for message in consumer:
            yield json.loads(message.value.decode('utf-8'))