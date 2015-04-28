package net.practice.jun;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.util.List;

//import io.advantageous.boon.json.JsonFactory.*;
//import static io.advantageous.boon.json.JsonFactory.fromJson;
//import io.fastjson.*;
import static org.boon.json.JsonFactory.fromJson;
import static org.boon.json.JsonFactory.fromJsonArray;

/**
 * Unit test for simple App.
 */
public class AppTest extends TestCase {

  public static Class<MyJson> myJson = MyJson.class;
  public static class MyJson  {
    int num;
    String str;

    @Override
    public String toString()  { return String.format("num %d, str %s", num, str); }
  }

  public void testBoon()  {
    final String jsonStr = "{'num':0, 'str':'str0'}";
    MyJson mj = fromJson(jsonStr, myJson);
    assertEquals(mj.num, 0);
    assertEquals(mj.str, "str0");

    final String jsonStrs = "[{'num':0, 'str':'str0'}, {'num':10, 'str':'str10'}, {'num':20, 'str':'str20'}]";
    List<MyJson> mjs = fromJsonArray(jsonStrs, myJson);
    assertEquals(mjs.get(2).num, 20);
    assertEquals(mjs.get(2).str, "str20");
  }
}
