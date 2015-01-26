package net.jun.practice;

import java.io.IOException;
import java.util.Map.Entry;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableMapReduceUtil;
import org.apache.hadoop.hbase.mapreduce.TableReducer;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.MapWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;

import org.apache.logging.log4j.Level;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Hdfs2TableMR  {
  private static Logger logger = LogManager.getLogger();

  private static String COLUMN_FAMILY_NAME = "doc";
  private static byte[] columnFamilyName = Bytes.toBytes(COLUMN_FAMILY_NAME);

  public static class Hdfs2TableMapper extends Mapper<LongWritable, Text, BytesWritable, MapWritable>  {
    private static BytesWritable[] columnKeys = null;
    private MapWritable outputMap = null;

    protected void setup(Context context) throws IOException, InterruptedException  {
      String[] strColumnKeys = { "c", "i", "t", "d", "u", "e" };
      columnKeys = new BytesWritable[strColumnKeys.length];
      for ( int i = 0; i < columnKeys.length; ++i )  {
        columnKeys[i] = new BytesWritable(Bytes.toBytes(strColumnKeys[i]));
      }
    }

    public void map(LongWritable keyIn, Text valueIn, Context context) throws IOException, InterruptedException  {
      String[] columnValues = valueIn.toString().split("\t");
      if ( 6 == columnValues.length && 0 < columnValues[1].length() )  {
        outputMap = new MapWritable();
        for ( int i = 0; i < columnValues.length; ++i )  {
          outputMap.put(columnKeys[i], new BytesWritable(Bytes.toBytes(columnValues[i])));
        }
        context.write((BytesWritable) outputMap.get(columnKeys[1]), outputMap);
      }
    }
  }

  public static class Hdfs2TableReducer extends TableReducer<BytesWritable, MapWritable, ImmutableBytesWritable>  {
    private static Configuration conf;
    private static BytesWritable idKey = new BytesWritable(Bytes.toBytes("i"));

    @Override
    protected void setup(Context context) throws IOException, InterruptedException  {
      conf = context.getConfiguration();
    }

    @Override
    protected void reduce(BytesWritable key, Iterable<MapWritable> values, Context context) throws IOException, InterruptedException  {
      //byte[] rowKey = ((BytesWritable) key.get(idKey)).getBytes();
      //Put put = new Put(rowKey);
      byte[] rowKey = key.getBytes();
      Put put = new Put(rowKey);
      int i = 0;
      for ( MapWritable value : values )  {
        for ( Entry entry : value.entrySet() )  {
          put.add(columnFamilyName, ((BytesWritable) entry.getKey()).getBytes(), ((BytesWritable) entry.getValue()).getBytes());
        }
        context.write(new ImmutableBytesWritable(rowKey), put);
      }
    }
  }

  public static void main(final String[] args) throws Exception  {
    Configuration conf = new Configuration();
    Job job = new Job(conf, "hdfs 2 table by MR");
    job.setJarByClass(Hdfs2TableMR.class);
    FileInputFormat.setInputPaths(job, new Path("hdfs:///some/directory/documents"));
    job.setInputFormatClass(TextInputFormat.class);
    job.setMapperClass(Hdfs2TableMapper.class);
    job.setMapOutputKeyClass(BytesWritable.class);
    job.setMapOutputValueClass(MapWritable.class);

    TableMapReduceUtil.initTableReducerJob("document", Hdfs2TableReducer.class, job);

    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
