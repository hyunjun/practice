if __name__ == '__main__':
  from confluent_kafka import Consumer, KafkaError

  c = Consumer({'bootstrap.servers': '<kafka server>', 'group.id': 'mygroup', 'default.topic.config': {'auto.offset.reset': 'smallest'}})
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
