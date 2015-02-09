# hbase example
* hdfs <-> hbase by pig and, java

## environments
* RedHat 6.4
* CDH5.3
  * Apache Pig version 0.12.0-cdh5.3.0 
  * Hadoop 2.5.0-cdh5.3.0
  * HBase 0.98.6-cdh5.3.0

## usage
* pig

  ```
  $ ./create_table.sh
  $ hadoop fs -put population_drift.txt /user/hanadmin
  $ pig -f hdfs2hbase.pig
  $ echo "count 'population_drift'" | hbase shell
  $ pig -f hbase2hdfs.pig
  # or pig -f hbase_columns2hdfs.pig  # specific columns of hbase to hdfs
  $ hadoop fs -ls population_drift
  ```
* java

  ```
  $ ./create_table.sh

  $ mvn package -DskipTests
  $ hadoop jar ./target/tableRW-1.0-SNAPSHOT-jar-with-dependencies.jar net.jun.practice.Hdfs2TableMR2
  # 다음 오류가 발생하는 경우
  # ... INFO zookeeper.ClientCnxn: Opening socket connection to server localhost.localdomain/127.0.0.1:2181. Will not attempt to authenticate using SASL (unknown error)
  # ...WARN zookeeper.ClientCnxn: Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect
java.net.ConnectException: Connection refused
  $ java -cp `hbase classpath`:./target/tableRW-1.0-SNAPSHOT-jar-with-dependencies.jar net.jun.practice.Hdfs2TableMR2

  $ hadoop jar ./target/tableRW-1.0-SNAPSHOT-jar-with-dependencies.jar net.jun.practice.Table2Hdfs
  $ hadoop fs -cat population_drift/part-m-00000
  ```
