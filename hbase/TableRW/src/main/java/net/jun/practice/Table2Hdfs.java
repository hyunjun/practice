package net.jun.practice;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map.Entry;
import java.util.NavigableMap;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.OptionBuilder;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
import org.apache.commons.cli.PosixParser;
import org.apache.commons.configuration.XMLConfiguration;
import org.apache.commons.configuration.ConfigurationException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HConstants;
import org.apache.hadoop.hbase.KeyValue;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.filter.FilterList;
import org.apache.hadoop.hbase.filter.CompareFilter.CompareOp;
import org.apache.hadoop.hbase.filter.PrefixFilter;
import org.apache.hadoop.hbase.filter.RegexStringComparator;
import org.apache.hadoop.hbase.filter.RowFilter;
//import org.apache.hadoop.hbase.filter.ValueFilter;
import org.apache.hadoop.hbase.filter.SingleColumnValueFilter;
import org.apache.hadoop.hbase.filter.SubstringComparator;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableInputFormat;
import org.apache.hadoop.hbase.mapreduce.TableMapReduceUtil;
import org.apache.hadoop.hbase.mapreduce.TableMapper;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.mapreduce.Job;
//import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
//import org.apache.hadoop.mapred.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import org.apache.logging.log4j.Level;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

//  http://www.cloudera.com/content/cloudera-content/cloudera-docs/HadoopTutorial/CDH4/Hadoop-Tutorial/ht_wordcount2_source.html
//  https://www.google.co.kr/search?q=cloudera+hbase+map+reduce+example&ie=utf-8&oe=utf-8&rls=org.mozilla:ko:official&client=firefox-a&channel=fflb&gws_rd=cr&ei=9XacUutGzpiIB7CQgYAE
//  http://archive.cloudera.com/cdh4/cdh/4/hbase/book.html#mapreduce.example
//  http://archive.cloudera.com/cdh/3/hbase/mapreduce.example.html
//  https://github.com/jrkinley/hbase-bulk-import-example/blob/master/src/main/java/com/cloudera/examples/hbase/bulkimport/Driver.java
public class Table2Hdfs  {
  private static Logger logger = LogManager.getLogger();
  private static final String COLUMN_FAMILY_NAME1 = "column-family-name1";
  private static final String COLUMN_FAMILY_NAME2 = "column-family-name2";

  private static byte[] tableName = Bytes.toBytes("population_drift");
  private static byte[] columnFamilyName1 = Bytes.toBytes("num");
  private static byte[] columnFamilyName2 = Bytes.toBytes("ratio");
  private static byte[] collectionType = null;
  private static String outputDir = "population_drift";

  public static class Map extends TableMapper<NullWritable, Text>  {
    private final static byte[] BYTE_TAB = Bytes.toBytes("\t");
    private static Configuration conf;
    private static byte[] columnFamilyName1 = null;
    private static byte[] columnFamilyName2 = null;
    Text tVal = new Text();

    @Override
    protected void setup(Context context) throws IOException, InterruptedException  {
      conf = context.getConfiguration();
      columnFamilyName1 = Bytes.toBytes(conf.get(COLUMN_FAMILY_NAME1));
      columnFamilyName2 = Bytes.toBytes(conf.get(COLUMN_FAMILY_NAME2));
    }

    @Override
    protected void map(ImmutableBytesWritable rowKey, Result result, Context context) throws IOException, InterruptedException  {
      tVal.clear();

      //  https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Result.html
      NavigableMap<byte[], NavigableMap<byte[], NavigableMap<Long, byte[]>>> resultMap = result.getMap();

      byte[] b = result.getRow();
      tVal.append(b, 0, b.length);
      for ( Entry<byte[], NavigableMap<byte[], NavigableMap<Long, byte[]>>> columnFamilyEntry : resultMap.entrySet() )  {
        NavigableMap<byte[],NavigableMap<Long, byte[]>> columnMap = columnFamilyEntry.getValue();
        for ( Entry<byte[], NavigableMap<Long, byte[]>> columnEntry : columnMap.entrySet() )  {
          NavigableMap<Long, byte[]> cellMap = columnEntry.getValue();
          for ( Entry<Long, byte[]> cellEntry : cellMap.entrySet() )  {
            tVal.append(BYTE_TAB, 0, BYTE_TAB.length);
            b = cellEntry.getValue();
            tVal.append(b, 0, b.length);
          }
        }
      }
      if ( 0 < tVal.getLength() )  context.write(NullWritable.get(), tVal);
    }
  }

  public static void main(final String[] args) throws Exception  {
    Configuration conf = HBaseConfiguration.create();
    String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
    logger.info(String.format("table %s:%s:%s %s into hdfs://%s", new String(tableName), new String(columnFamilyName1), new String(columnFamilyName2), null == collectionType ? "" : "collection " + new String(collectionType), outputDir));

    MyHBaseConfiguration myHbaseConf = new MyHBaseConfiguration("hbase-config.xml");
    conf.set(HConstants.ZOOKEEPER_QUORUM, myHbaseConf.getZookeeperQuorum());
    conf.set(HConstants.ZOOKEEPER_CLIENT_PORT, myHbaseConf.getZookeeperClientPort());
    //  remote hdfs access
    //conf.set("fs.defaultFS", "hdfs://10.29.2.226:8020/user/hanadmin");
    //conf.set("hadoop.job.ugi", "hanadmin");

    conf.set(COLUMN_FAMILY_NAME1, new String(columnFamilyName1));
    conf.set(COLUMN_FAMILY_NAME2, new String(columnFamilyName2));

    Job job = new Job(conf, "table 2 hdfs");
    job.setJarByClass(Table2Hdfs.class);
    job.setInputFormatClass(TableInputFormat.class);

    final Scan scan = new Scan();
    scan.setCacheBlocks(false);  //  because it's full scan
    if ( null != collectionType )  {
      scan.setFilter(new PrefixFilter(collectionType));
    }

    TableMapReduceUtil.initTableMapperJob(tableName, scan, Map.class, NullWritable.class, Text.class, job);
    job.setOutputKeyClass(NullWritable.class);
    job.setOutputValueClass(Text.class);
    job.setOutputFormatClass(TextOutputFormat.class);
    job.setNumReduceTasks(0);

    FileSystem fs = FileSystem.get(new Configuration());
    System.out.println(fs.getHomeDirectory().getName());
    final Path outPath = new Path(outputDir);
    if ( fs.exists(outPath) )
      logger.error("output directory[" + outputDir + "] already exists");
    TextOutputFormat.setOutputPath(job, outPath);

    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
