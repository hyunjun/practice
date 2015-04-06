package test.json;

import java.util.List;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import com.jayway.jsonpath.*;

//	https://github.com/jayway/JsonPath
public class JsonPathTest extends TestCase  {
  public void testJsonPath()  {
    final String jsonStr = "{ \"store\": { \"book\": [ { \"category\": \"reference\", \"author\": \"Nigel Rees\", \"title\": \"Sayings of the Century\", \"price\": 8.95 }, { \"category\": \"fiction\", \"author\": \"Evelyn Waugh\", \"title\": \"Sword of Honour\", \"price\": 12.99, \"isbn\": \"0-553-21311-3\" } ], \"bicycle\": { \"color\": \"red\", \"price\": 19.95 } } }";
    assertNotNull(jsonStr);
    List<String> authors = JsonPath.read(jsonStr, "$.store.book[*].author");
    assertEquals("Nigel Rees", authors.get(0));
    assertEquals("Evelyn Waugh", authors.get(1));
  }

  class Test  {
    public final int t;
    Test(int t) { this.t = t; }
  }

  public void testArray() {
    final String jsonStr = "[{'int':0, 'str':'str0'}, {'int':1, 'str':'str1'}, {'int':2, 'str':'str2'}]";
    System.out.println(JsonPath.parse(jsonStr).read("$[1].int"));

    Object document = Configuration.defaultConfiguration().jsonProvider().parse(jsonStr);
    System.out.println(JsonPath.read(document, "$[0].int"));
    System.out.println(JsonPath.read(document, "$[1].str"));

    List<Object> tests = JsonPath.read(document, "$[*]");
    for ( Object test : tests )  {
      int t = JsonPath.read(test, "$.int");
      String s = JsonPath.read(test, "$.str");
      System.out.println(t + "\t" + s);
    }
  }
}
