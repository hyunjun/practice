package net.jun.practice;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableMapReduceUtil;
import org.apache.hadoop.hbase.mapreduce.TableReducer;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;

import org.apache.logging.log4j.Level;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Hdfs2Table2  {
  private static Logger logger = LogManager.getLogger();

  private static String COLUMN_FAMILY_NAME = "doc";
  private static byte[] columnFamilyName = Bytes.toBytes(COLUMN_FAMILY_NAME);

  public static class Hdfs2TableMapper extends Mapper<LongWritable, Text, Text, IntWritable>  {
    private final static IntWritable one = new IntWritable(1);

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException  {
      context.write(value, one);
    }
  }

  public static class Hdfs2TableReducer extends TableReducer<Text, Text, ImmutableBytesWritable>  {
    private static Configuration conf;
    private static byte[][] columnKeys = null;

    @Override
    protected void setup(Context context) throws IOException, InterruptedException  {
      conf = context.getConfiguration();
      String[] strColumnKeys = { "c", "i", "t", "d", "u", "e" };
      columnKeys = new byte[6][];
      for ( int i = 0; i < columnKeys.length; ++i )  {
        columnKeys[i] = Bytes.toBytes(strColumnKeys[i]);
      }
    }

    @Override
    protected void reduce(Text value, Iterable<Text> values, Context context) throws IOException, InterruptedException  {
      String[] columnValues = value.toString().split("\t");
      if ( 6 == columnValues.length && 0 < columnValues[1].length() )  {
        Put put = new Put(Bytes.toBytes(columnValues[1]));
        for ( int j = 0; j < columnValues.length; ++j )  {
          put.add(columnFamilyName, columnKeys[j], Bytes.toBytes(columnValues[j]));
        }
        context.write(new ImmutableBytesWritable(Bytes.toBytes(columnValues[1])), put);
      }
    }
  }

  public static void main(final String[] args) throws Exception  {
    Configuration conf = new Configuration();
    Job job = new Job(conf, "hdfs 2 table");
    job.setJarByClass(Hdfs2Table2.class);
    FileInputFormat.setInputPaths(job, new Path("hdfs:///some/directory/documents"));
    job.setInputFormatClass(TextInputFormat.class);
    job.setMapperClass(Hdfs2TableMapper.class);
    job.setMapOutputKeyClass(Text.class);
    job.setMapOutputValueClass(IntWritable.class);

    TableMapReduceUtil.initTableReducerJob("document", Hdfs2TableReducer.class, job);

    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
