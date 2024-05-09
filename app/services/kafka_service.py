from confluent_kafka import Consumer, KafkaError, Producer
import os
from dotenv import load_dotenv
import json

load_dotenv()
BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS")

class KafkaService:
    def __init__(self, bootstrap_servers=BOOTSTRAP_SERVERS, group_id='my_group_id'):
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id

    def send(self, topic, message):
        print("send: ", message)
        producer = Producer({'bootstrap.servers': self.bootstrap_servers})
        producer.produce(topic, json.dumps(message).encode('utf-8'))
        producer.flush()

    def receive(self, topic):
        consumer = Consumer({
            'bootstrap.servers': self.bootstrap_servers,
            'group.id': self.group_id,  # Se establece el ID de grupo aquí
            'auto.offset.reset': 'earliest'
        })
        consumer.subscribe([topic])
        try:
            while True:
                message = consumer.poll(timeout=1.0)
                if message != None:
                    print("receive: ", message.value().decode('utf-8'))
                    return message.value().decode('utf-8')
                if message is None:
                    continue
                if message.error():
                    if message.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        break                
        
        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()
