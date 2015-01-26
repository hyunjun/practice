package net.jun.practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InterruptedIOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.Row;
import org.apache.hadoop.hbase.util.Bytes;

import org.apache.logging.log4j.Level;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Hdfs2Table  {
  private static Logger logger = LogManager.getLogger();

  public static void main(final String[] args) throws IOException, InterruptedException, InterruptedIOException  {
    FileSystem fs = FileSystem.get(new Configuration());
    FileStatus[] status = fs.listStatus(new Path("/some/directory/documents"));

    HBaseConfiguration hbaseConf = new HBaseConfiguration();
    HTable htable = new HTable(hbaseConf, "document");
    htable.setAutoFlush(false);
    byte[] columnFamilyName = Bytes.toBytes("doc");
    String[] strColumnKeys = { "c", "i", "t", "d", "u", "e" };
    byte[][] columnKeys = new byte[6][];
    for ( int i = 0; i < columnKeys.length; ++i )  {
        columnKeys[i] = Bytes.toBytes(strColumnKeys[i]);
    }

    long count = 0;
    final List<Row> batches = new ArrayList<Row>();
    for ( int i = 0; i < status.length; ++i )  {
      String[] splits = status[i].getPath().toString().split("/");
      if ( false == splits[splits.length - 1].startsWith("part-m-") )
        continue;
      BufferedReader br = new BufferedReader(new InputStreamReader(fs.open(status[i].getPath())));
      String line = null;
      while ( null != (line = br.readLine()) )  {
        String[] columnValues = line.split("\t");
        if ( 6 != columnValues.length || columnValues[1].length() <= 0 )
          continue;
        Put put = new Put(Bytes.toBytes(columnValues[1]));
        for ( int j = 0; j < columnValues.length; ++j )  {
          //System.out.println("[" + j + "]\t" + columnKeys[j] + "\t[" + j + "]\t" + columnValues[j]);
          put.add(columnFamilyName, columnKeys[j], Bytes.toBytes(columnValues[j]));
        }
        batches.add(put);
        if ( 500 < batches.size() )  {
          Object[] results = new Object[batches.size()];
          htable.batch(batches, results);
          batches.clear();
        }
        //htable.put(put);
        ++count;
        //if ( count % 10000000 == 0 )  System.out.println("counts\t" + count);
        logger.info(String.format("count %d", count));
      }
      br.close();
      if ( 0 < batches.size() )  {
        Object[] results = new Object[batches.size()];
        htable.batch(batches, results);
        batches.clear();
      }
    }

    htable.flushCommits();
    htable.close();
  }
}
