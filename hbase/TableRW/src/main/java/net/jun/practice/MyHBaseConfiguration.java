package net.jun.practice;

import org.apache.commons.configuration.XMLConfiguration;
import org.apache.commons.configuration.ConfigurationException;

import org.apache.logging.log4j.Level;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

//  http://hbase.apache.org/0.94/apidocs/index.html?overview-summary.html
public class MyHBaseConfiguration  {
  private static Logger logger = LogManager.getLogger();

  private XMLConfiguration xmlConfiguration = null;
  private String zookeeperQuorum = null;
  private String zookeeperClientPort = null;
  private int htablePoolNum;

  public MyHBaseConfiguration(final String xmlFileName)  {
    try  {
      xmlConfiguration = new XMLConfiguration(getClass().getClassLoader().getResource(xmlFileName));
      StringBuilder sb = new StringBuilder();
      if ( null == xmlConfiguration.getString("zookeeper.quorum(0)") )  {
        logger.error("zookeeper configuration error");
        throw new ConfigurationException();
      }
      for ( int i = 0; i < 3; ++i )  {
        if ( null != xmlConfiguration.getString("zookeeper.quorum(" + i + ")") )  {
          if ( 0 < i )  sb.append(",");
          sb.append(xmlConfiguration.getString("zookeeper.quorum(" + i + ")"));
        }
      }
      zookeeperQuorum = sb.toString();
      zookeeperClientPort = xmlConfiguration.getString("zookeeper.client_port");
      htablePoolNum = xmlConfiguration.getInt("htable_pool_num");

    } catch (ConfigurationException e)  {
      logger.error(e);
    }
  }
  public String getZookeeperQuorum()  {
    logger.debug("zookeeper quorum " + zookeeperQuorum);
    return  zookeeperQuorum;
  }
  public String getZookeeperClientPort()  {  return  zookeeperClientPort;  }
  public int getHTablePoolNum()  {  return  htablePoolNum;  }
}
