# SimpleApp
* https://spark.apache.org/docs/1.2.0/quick-start.html
* execution, CDH 5.3 (spark 1.2.0, hadoop 2.5.0), RedHad 6.4
  * local `/usr/lib/spark/bin/spark-submit --class "SimpleApp" --master local[4] ./target/scala-2.10/simple-project_2.10-1.0.jar`
  * yarn-client

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
  * yarn-cluster; 동작하지만 결과 출력이 없음

    ```
    # the same configuration with yarn-client
    $ /usr/lib/spark/bin/spark-submit --class SimpleApp --master yarn-client --num-executors 6 --driver-memory 4g --executor-memory 2g --executor-cores 1 --queue thequeue ./target/scala-2.10/simple-project_2.10-1.0.jar
    ```
