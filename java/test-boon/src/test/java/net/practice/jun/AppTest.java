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

  public static Class<Input> classInput = Input.class;
  public class Input {
    public WAtt w_att;
    public String input;
    public List<Term> terms;

    public final class WAtt {
      public int pos;
      public int offset;
    }

    public final class Term {
      public String type;
      public String str;
      public List<Term> terms;
      public Syn syn;

      public final class Syn {
        public String m_syn;
        public List<String> terms;
        public List<String> s_syn;
      }
    }
  }

  public void testBoon2() {
    final String jsonStrs = "[{\"w_att\":{\"pos\":0,\"offset\":0},\"input\":\"ES검색은\",\"terms\":[{\"type\":\"NE\",\"str\":\"다음\",\"syn\":{\"m_syn\":\"ES\",\"terms\":[\"ES\"],\"s_syn\":[\"daum\"]}},{\"type\":\"N\",\"str\":\"검색\"},{\"type\":\"SU\",\"str\":\"검색은\"}]},{\"w_att\":{\"pos\":6,\"offset\":16},\"input\":\"정확하고\",\"terms\":[{\"type\":\"RO\",\"str\":\"정확하다\"},{\"type\":\"SU\",\"str\":\"정확하고\"}]},{\"w_att\":{\"pos\":11,\"offset\":29},\"input\":\"빠르다\",\"terms\":[{\"type\":\"RO\",\"str\":\"빠르다\"},{\"type\":\"SU\",\"str\":\"빠르다\"}]}]";
    List<Input> inputs = fromJsonArray(jsonStrs, classInput);
    assertEquals(inputs.get(0).w_att.pos, 0);
    assertEquals(inputs.get(0).w_att.offset, 0);
    assertEquals(inputs.get(0).input, "ES검색은");
    assertEquals(inputs.get(0).terms.get(0).type, "NE");
    assertEquals(inputs.get(0).terms.get(0).str, "다음");
    assertEquals(inputs.get(0).terms.get(0).syn.m_syn, "ES");
    assertEquals(inputs.get(0).terms.get(0).syn.terms.get(0), "ES");
    assertEquals(inputs.get(0).terms.get(0).syn.s_syn.get(0), "daum");
    assertEquals(inputs.get(0).terms.get(1).type, "N");
    assertEquals(inputs.get(0).terms.get(1).str, "검색");
    assertEquals(inputs.get(0).terms.get(2).type, "SU");
    assertEquals(inputs.get(0).terms.get(2).str, "검색은");
    assertEquals(inputs.get(1).w_att.pos, 6);
    assertEquals(inputs.get(1).w_att.offset, 16);
    assertEquals(inputs.get(1).input, "정확하고");
    assertEquals(inputs.get(2).w_att.pos, 11);
    assertEquals(inputs.get(2).w_att.offset, 29);
    assertEquals(inputs.get(2).input, "빠르다");
  }
}
