__api__ = 'https://pykafka.readthedocs.io/en/latest/'

import json
from pykafka import KafkaClient

client = KafkaClient(hosts='10.41.17.57:9092')
print(client.topics)

topic = client.topics[b'nano_test']
partitions = topic.partitions
print(u"查看所有分区 {}".format(partitions))

earliest_offset = topic.earliest_available_offsets()
print(u"获取最早可用的offset {}".format(earliest_offset))

last_offset = topic.latest_available_offsets()
print(u"最近可用offset {}".format(last_offset))


# 同步生产消息
with topic.get_sync_producer() as producer:
    for i in range(4):
        producer.produce(json.dumps({'test': i}).encode())

last_offset = topic.latest_available_offsets()
print(u"最近可用offset {}".format(last_offset))

# 占有 topic 100% 的消息
consumer = topic.get_simple_consumer(b"simple_consumer_group")
for message in consumer:
    if message:
        print(message.offset, message.value)

