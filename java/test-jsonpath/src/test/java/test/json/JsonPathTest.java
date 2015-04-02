package test.json;

import java.util.List;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import com.jayway.jsonpath.JsonPath;

//	https://github.com/jayway/JsonPath
public class JsonPathTest extends TestCase  {
  public void testJsonPath()  {
    final String jsonStr = "{ \"store\": { \"book\": [ { \"category\": \"reference\", \"author\": \"Nigel Rees\", \"title\": \"Sayings of the Century\", \"price\": 8.95 }, { \"category\": \"fiction\", \"author\": \"Evelyn Waugh\", \"title\": \"Sword of Honour\", \"price\": 12.99, \"isbn\": \"0-553-21311-3\" } ], \"bicycle\": { \"color\": \"red\", \"price\": 19.95 } } }";
    assertNotNull(jsonStr);
    List<String> authors = JsonPath.read(jsonStr, "$.store.book[*].author");
    assertEquals("Nigel Rees", authors.get(0));
    assertEquals("Evelyn Waugh", authors.get(1));
  }
}
