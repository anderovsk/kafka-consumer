from kafka import KafkaConsumer
import os


def consumer():
    bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS')
    topic = os.getenv('TOPIC')
    # topic = 'anderovsk'
    # bootstrap_servers = ['localhost:9092']
    print(bootstrap_servers)
    print(topic)
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')
    for msg in consumer:
        print(msg.value)
    return(msg.value)

consumer()