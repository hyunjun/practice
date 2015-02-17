package net.jun.practice;

import java.net.URL;

import org.apache.commons.codec.binary.Base64;

import org.apache.xmlrpc.client.XmlRpcClient;
import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;

public class App  {
  public static void main( String[] args ) throws Exception  {
    XmlRpcClientConfigImpl xmlRpcConfig = null;
    XmlRpcClient client = null;

    xmlRpcConfig = new XmlRpcClientConfigImpl();
    xmlRpcConfig.setServerURL(new URL("http://localhost:49944/xmlrpc_test"));
    client = new XmlRpcClient();
    client.setConfig(xmlRpcConfig);

    Object[] params = new Object[]{(Object) new String(Base64.encodeBase64(args[0].getBytes()))};
    for ( Object o : (Object[]) client.execute("analyze", params) ) {
      System.out.println(o);
    }
  }
}
