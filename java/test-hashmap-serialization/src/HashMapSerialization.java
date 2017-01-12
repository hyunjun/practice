import java.io.*;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by jun on 2017. 1. 12..
 * http://beginnersbook.com/2013/12/how-to-serialize-hashmap-in-java/
 * 작은 entry에 대해서는 당연히 잘 되지만 얼마나 많은 개수의 entry를 다룰 지는 test 필요
 * jvm option에 따라 달라질 것
 */
public class HashMapSerialization {
  public static void main(String[] args)  {
    HashMap<String, Integer> map = new HashMap<String, Integer>();
    map.put("test", 1);
    map.put("다음", 2);
    try {
      FileOutputStream fos = new FileOutputStream("hashmap.ser");
      ObjectOutputStream oos = new ObjectOutputStream(fos);
      oos.writeObject(map);
      oos.close();
      fos.close();
    } catch ( IOException ioe ) {
      ioe.printStackTrace();
    }

    map = null;
    try {
      FileInputStream fis = new FileInputStream("hashmap.ser");
      ObjectInputStream ois = new ObjectInputStream(fis);
      map = (HashMap) ois.readObject();
      ois.close();
      fis.close();
    } catch ( FileNotFoundException fnfe )  {

    } catch ( IOException ioe ) {

    } catch ( ClassNotFoundException cnfe ) {

    }
    for ( Map.Entry entry : map.entrySet() )  {
      System.out.println("key " + entry.getKey() + "\tvalue " + entry.getValue());
    }
  }
}
