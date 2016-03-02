package com.practice.jun;

//  original; http://www.javaworld.com/article/2072602/java-properties-in-xml.html
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.Properties;

public class PropertiesExamples
{
  /** No-arguments constructor. */
  public PropertiesExamples() {}

  /**
   * Get traditional properties in name=value format.
   *
   * @param filePathAndName Path and name of properties file (without the .properties extension).
   * @return Properties read in from provided file.
   **/
  public Properties loadTraditionalProperties(final String filePathAndName)
  {
    final Properties properties = new Properties();
    try
    {
      final FileInputStream in = new FileInputStream(filePathAndName);
      properties.load(in);
      in.close();
    }
    catch (FileNotFoundException fnfEx)
    {
      System.err.println("Could not read properties from file " + filePathAndName);
    }
    catch (IOException ioEx)
    {
      System.err.println(
          "IOException encountered while reading from " + filePathAndName);
    }
    return properties;
  }

  /**
   * Store provided properties in XML format.
   *
   * @param sourceProperties Properties to be stored in XML format.
   * @param out OutputStream to which to write XML formatted properties.
   **/
  public void storeXmlProperties(final Properties sourceProperties, final OutputStream out)
  {
    try
    {
      sourceProperties.storeToXML(out, "This is easy!");
    }
    catch (IOException ioEx)
    {
      System.err.println("ERROR trying to store properties in XML!");
    }
  }

  /**
   * Store provided properties in XML format to provided file.
   *
   * @param sourceProperties Properties to be stored in XML format.
   * @param pathAndFileName Path and name of file to which XML-formatted properties will be written.
   **/
  public void storeXmlPropertiesToFile(final Properties sourceProperties, final String pathAndFileName)
  {
    try
    {
      FileOutputStream fos = new FileOutputStream(pathAndFileName);
      storeXmlProperties(sourceProperties, fos);
      fos.close();
    }
    catch (FileNotFoundException fnfEx)
    {
      System.err.println("ERROR writing to " + pathAndFileName);
    }
    catch (IOException ioEx)
    {
      System.err.println("ERROR trying to write XML properties to file " + pathAndFileName);
    }
  }

  /**
   * Runs main examples.
   *
   * @param arguments Command-line arguments; none anticipated.
   **/
  public static void main(final String[] arguments)
  {
    final PropertiesExamples me = new PropertiesExamples();
    final Properties inputProperties = me.loadTraditionalProperties("src/test/java/resource/examples.properties");
    for ( Object key : inputProperties.keySet() )
      System.out.println(key + "\t" + inputProperties.get(key));
    me.storeXmlPropertiesToFile(inputProperties, "src/test/java/resource/examples-xml.properties");
  }
}
