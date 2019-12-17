from kafka import KafkaProducer

topic = 'test2'
bootstrap_servers = ['192.168.1.129:9092']


def send(msg=None, callback=None):
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers, acks='all')
    future = producer.send(topic=topic, key=b'my_key', value=str.encode(msg))
    result = future.get(timeout=20)
    callback(result)
    return "Send had successed!"


def callback(result):
    print(result)
    return result


# if __name__ == '__main__':
#     send('aabggb', callback)
