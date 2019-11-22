from json import dumps
import uuid
from kafka import KafkaConsumer
from kafka import KafkaProducer

server_list = ['192.168.1.129:9092']

# 生产者
producer = KafkaProducer(bootstrap_servers=server_list,
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

n = 10
i = 0
while i <= n:
    uuidstr = uuid.uuid5(uuid.NAMESPACE_DNS, "python.org")
    msg = {'name': str(uuidstr), 'text': str(uuidstr)}
    producer.send('test2', msg)
    i = i + 1
# 消费者
consumer = KafkaConsumer('test2',
                         auto_offset_reset='earliest',
                         bootstrap_servers=server_list,
                         group_id='test-group3')
print(consumer)
for msg in consumer:
    print(msg)
