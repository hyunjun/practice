# SimpleApp
* https://spark.apache.org/docs/1.2.0/quick-start.html
* execution

  ```
  # if undefined
  $ export JAVA_HOME=/usr/java/jdk1.8.0_25
  $ export HADOOP_CONF_DIR=/etc/hadoop/conf

  # if proxy necessary
  $ export https_proxy=https://x.y.z.w:port_number
  $ export http_proxy=http://x.y.z.w:port_number

  $ sbt package
  $ /usr/lib/spark/bin/spark-submit --class SimpleApp --master yarn-client --num-executors 6 --driver-memory 4g --executor-memory 2g --executor-cores 1 --queue thequeue ./target/scala-2.10/simple-project_2.10-1.0.jar
  ```
