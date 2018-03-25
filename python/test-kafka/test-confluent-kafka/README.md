# test confluent kafka

* execution

  ```
  $ docker build -t test-confluent-kafka:latest .
  $ docker run -d --rm --name test-confluent-kafka test-confluent-kafka

  $ docker exec -it test-confluent-kafka /bin/bash
  $ docker stop test-confluent-kafka
  ```
