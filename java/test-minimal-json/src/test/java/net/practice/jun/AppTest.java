package net.practice.jun;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import com.eclipsesource.json.*;

public class AppTest extends TestCase {

  public AppTest( String testName ) {
    super( testName );
  }

  public void testCreateJson() {
    JsonObject jsonObject = new JsonObject().add("name", "John").add("age", 23);
    assertEquals("John", jsonObject.get("name").asString());
    assertEquals(23, jsonObject.get("age").asInt());
  }
}
