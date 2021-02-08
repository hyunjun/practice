package net.practice.jun;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.io.IOException;
import java.io.StringReader;

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

  public void testReadJson() throws IOException  {
    //final String jsonStr = "[{\"w_att\":{\"pos\":0,\"offset\":0},\"input\":\"철수가\",\"terms\":[{\"type\":\"N\",\"str\":\"철수\"},{\"type\":\"SU\",\"str\":\"철수가\"}]},{\"w_att\":{\"pos\":4,\"offset\":10},\"input\":\"밥을\",\"terms\":[{\"type\":\"N\",\"str\":\"밥\"},{\"type\":\"SU\",\"str\":\"밥을\"}]},{\"w_att\":{\"pos\":7,\"offset\":17},\"input\":\"먹었다\",\"terms\":[{\"type\":\"RO\",\"str\":\"먹다\"},{\"type\":\"SU\",\"str\":\"먹었다\"}]}]";
    final String jsonStr = "[{\"w_att\":{\"pos\":0,\"offset\":0},\"input\":\"농업협동조합은\",\"terms\":[{\"type\":\"NE\",\"str\":\"농업협동조합\",\"terms\":[{\"type\":\"N\",\"str\":\"농업\"},{\"type\":\"N\",\"str\":\"협동\"},{\"type\":\"N\",\"str\":\"조합\"}],\"syn\":{\"m_syn\":\"농협\",\"terms\":[\"농협\"]}},{\"type\":\"SU\",\"str\":\"농업협동조합은\",\"syn\":{\"m_syn\":\"농협은\"}}]},{\"w_att\":{\"pos\":8,\"offset\":22},\"input\":\"금리가\",\"terms\":[{\"type\":\"N\",\"str\":\"금리\"},{\"type\":\"SU\",\"str\":\"금리가\"}]},{\"w_att\":{\"pos\":12,\"offset\":32},\"input\":\"높다\",\"terms\":[{\"type\":\"RO\",\"str\":\"높다\"},{\"type\":\"SU\",\"str\":\"높다\"}]}]";
    //JsonObject jsonObj = JsonObject.readFrom(jsonStr);
    //assertNotNull(jsonObj);
    JsonArray jsonArr = JsonArray.readFrom(new StringReader(jsonStr));
    assertNotNull(jsonArr);
    for ( JsonValue val : jsonArr ) {
      JsonObject jsonObj = val.asObject();
      System.out.println(jsonObj);

      //  Input
      JsonObject wAtt = jsonObj.get("w_att").asObject();
      System.out.println("w_att\t" + wAtt.get("pos") + "\t" + wAtt.get("offset"));

      String input = jsonObj.get("input").asString();
      System.out.println("input\t" + input);

      JsonArray terms = jsonObj.get("terms").asArray();
      System.out.println("terms");
      for ( JsonValue tVal : terms )  {
        //  TermOfInput
        JsonObject tObj = tVal.asObject();
        System.out.println("\t" + tObj.get("type") + "\t" + tObj.get("str"));
        JsonValue tTermsVal = tObj.get("terms");
        if ( null != tTermsVal )  {
          System.out.println("\tterms");
          JsonArray tArr = tTermsVal.asArray();
          for ( JsonValue ttVal : tArr )  {
            JsonObject ttValObj = ttVal.asObject();
            System.out.println("\t\t" + ttValObj.get("type") + "\t" + ttValObj.get("str"));
          }
        }
        JsonValue tSynVal = tObj.get("syn");
        if ( null != tSynVal )  {
          System.out.println("\tsyn");
          JsonObject syn = tSynVal.asObject();
          System.out.println("\t\t" + syn.get("m_syn"));
          JsonValue tsTerms = syn.get("terms");
          if ( null != tsTerms )  {
            System.out.println("\t\tterms");
            JsonArray tsTermsArr = tsTerms.asArray();
            for ( JsonValue tstVal : tsTermsArr ) {
              System.out.println("\t\t\t" + tstVal.asString());
            }
          }
        }
      }
    }
  }
}
