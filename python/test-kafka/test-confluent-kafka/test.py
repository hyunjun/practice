if __name__ == '__main__':
  from confluent_kafka import Consumer, KafkaError

  # 'enable.partition.eof': False
  # https://github.com/confluentinc/confluent-kafka-python/issues/283
  # https://github.com/confluentinc/confluent-kafka-python/issues/176
  # https://github.com/edenhill/librdkafka/issues/1024
  c = Consumer({'bootstrap.servers': '<kafka server>', 'group.id': 'mygroup', 'enable.partition.eof': False, 'default.topic.config': {'auto.offset.reset': 'smallest'}})
  c.subscribe(['<topic>'])
  running = True
  while running:
    msg = c.poll()
    if not msg.error():
      print('Received message: %s' % msg.value().decode('utf-8'))
    elif msg.error().code() != KafkaError._PARTITION_EOF:
      print(msg.error())
      running = False
  c.close()
