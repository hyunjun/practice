#!/bin/sh

CUR_DIR=$(readlink -f $(dirname $(readlink -f ${BASH_SOURCE[0]})))
INPUT=test_data
OUTPUT=test_output
#HADOOP_STREAMING=/usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.5.0.jar
HADOOP_STREAMING=/usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar
MAPPER=mapper2.py
EXTERNAL=external.py

hadoop fs -rm $INPUT
hadoop fs -put $INPUT

hadoop fs -rm -r $OUTPUT
hadoop jar $HADOOP_STREAMING \
  -files $MAPPER,$EXTERNAL \
  -input $INPUT \
  -output $OUTPUT \
  -mapper $MAPPER \
  -numReduceTasks 0

hadoop fs -rm -r $OUTPUT
rm pig_*.log
pig -f streaming.pig -param proc=$MAPPER -param procpath=$CUR_DIR/$MAPPER -param externalpath=$CUR_DIR/$EXTERNAL -param data=$INPUT -param output=$OUTPUT
