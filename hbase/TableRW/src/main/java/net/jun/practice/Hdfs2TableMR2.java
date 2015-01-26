package net.jun.practice;

import java.io.IOException;
import java.util.Map.Entry;

import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.HConstants;
import org.apache.hadoop.hbase.client.HTableInterface;
import org.apache.hadoop.hbase.client.HConnection;
import org.apache.hadoop.hbase.client.HConnectionManager;
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
import org.apache.hadoop.mapreduce.lib.output.NullOutputFormat;

import org.apache.logging.log4j.Level;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Hdfs2TableMR2  {
  private static Logger logger = LogManager.getLogger();

  private static String[] COLUMN_FAMILY_NAME = { "num", "ratio" };
  private static byte[] columnFamilyName1 = Bytes.toBytes(COLUMN_FAMILY_NAME[0]);
  private static byte[] columnFamilyName2 = Bytes.toBytes(COLUMN_FAMILY_NAME[1]);

  public static class Hdfs2TableMapper extends Mapper<LongWritable, Text, ImmutableBytesWritable, Put>  {
    private HTableInterface table = null;
    private HConnection hConnection = null;
    private static byte[][] columnKeys = null;
    private MapWritable outputMap = null;

    protected void setup(Context context) throws IOException, InterruptedException  {
      Configuration conf = HBaseConfiguration.create();
      MyHBaseConfiguration myHbaseConf = new MyHBaseConfiguration("hbase-config.xml");
      conf.set(HConstants.ZOOKEEPER_QUORUM, myHbaseConf.getZookeeperQuorum());
      conf.set(HConstants.ZOOKEEPER_CLIENT_PORT, myHbaseConf.getZookeeperClientPort());
      //conf.set("hbase.zookeeper.quorum", "x.y.z.w1,x.y.z.w2,x.y.z.w3");
      hConnection = HConnectionManager.createConnection(conf);
      table = hConnection.getTable("population_drift");

      String[] strColumnKeys = { "region", "n_in", "n_out", "n_net", "n_prev", "r_in", "r_out", "r_net", "r_prev" };
      columnKeys = new byte[strColumnKeys.length][];
      for ( int i = 0; i < columnKeys.length; ++i )  {
        columnKeys[i] = Bytes.toBytes(strColumnKeys[i]);
      }
    }

    public void map(LongWritable keyIn, Text valueIn, Context context) throws IOException, InterruptedException  {
      String[] columnValues = valueIn.toString().split("\t");
      if ( 9 == columnValues.length ) {
        byte[] rowKey = Bytes.toBytes(columnValues[0]);
        Put put = new Put(rowKey);

        for ( int i = 1; i < 5; ++i )  {
          put.add(columnFamilyName1, columnKeys[i], Bytes.toBytes(columnValues[i]));
        }
        for ( int i = 5; i < columnValues.length; ++i )  {
          put.add(columnFamilyName2, columnKeys[i], Bytes.toBytes(columnValues[i]));
        }
        //context.write(new ImmutableBytesWritable(rowKey), put);
        table.put(put);
      }
    }
  }

  public static void main(final String[] args) throws Exception  {
    Configuration conf = new Configuration();
    Job job = new Job(conf, "hdfs 2 table by MR");
    job.setJarByClass(Hdfs2TableMR2.class);
    FileInputFormat.setInputPaths(job, new Path("hdfs:///some/directory/population_drift.txt"));
    job.getConfiguration().setBoolean("mapred.map.tasks.speculative.execution", false);
    job.setInputFormatClass(TextInputFormat.class);
    job.setMapperClass(Hdfs2TableMapper.class);
    job.setMapOutputKeyClass(NullOutputFormat.class);
    job.setNumReduceTasks(0);

    TableMapReduceUtil.initTableReducerJob("population_drift", null, job);

    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
