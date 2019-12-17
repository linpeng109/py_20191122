from kafka import KafkaConsumer

topics = ['test2']
bootstrap_servers = ['192.168.1.129:9092']


def receive():
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, auto_offset_reset="earliest")
    consumer.subscribe(topics=topics)
    for msg in consumer:
        print(msg)

if __name__ == '__main__':
    receive()
