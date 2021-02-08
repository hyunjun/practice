#!/bin/sh

HOME_PATH=`pwd`
HADOOP_HOME=/usr/lib/hadoop-0.20-mapreduce
HADOOP_FILE_PATH=/path/to/data
HADOOP_OUTPUT=/path/to/output
MAPPER=$HOME_PATH/map.pl
REDUCER=$HOME_PATH/reduce.pl

hadoop fs -rm -r $HADOOP_OUTPUT
hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming*-*.jar \
  -file $MAPPER -mapper $MAPPER \
  -file $REDUCER -reducer $REDUCER \
  -input $HADOOP_FILE_PATH -output $HADOOP_OUTPUT \
  -cmdenv LC_ALL=ko_KR.utf8

#PIG_OUTPUT=/tmp/pig_sort_output
#hadoop fs -rm -r $PIG_OUTPUT
#pig -f pig_sort.pig -param input=$HADOOP_OUTPUT -param output=$PIG_OUTPUT
