package net.practice.yaml;

import org.junit.Test;

import static org.junit.Assert.*;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.yaml.snakeyaml.Yaml;

//  https://bitbucket.org/asomov/snakeyaml/src/c647d2373ca66f57a8344860f8cc8dce7e9c370a/src/test/java/examples/LoadExampleTest.java?at=default
public class AppTest  {

  @Test
  public void testLoad() {
    Yaml yaml = new Yaml();
    String document = "\n- Hesperiidae\n- Papilionidae\n- Apatelodidae\n- Epiplemidae";
    List<String> list = (List<String>) yaml.load(document);
    assertEquals("[Hesperiidae, Papilionidae, Apatelodidae, Epiplemidae]", list.toString());
  }

  @Test
  public void testLoadFromString() {
    Yaml yaml = new Yaml();
    String document = "hello: 25";
    @SuppressWarnings("unchecked")
    Map<String, Integer> map = (Map<String, Integer>) yaml.load(document);
    assertEquals("{hello=25}", map.toString());
    assertEquals(new Integer(25), map.get("hello"));
  }

  @Test
  public void testLoadFromStream() throws IOException {
    InputStream input = new FileInputStream(new File("src/test/resource/utf-8.txt"));
    Yaml yaml = new Yaml();
    Object data = yaml.load(input);
    assertEquals("test", data);
    data = yaml.load(new ByteArrayInputStream("test2".getBytes("UTF-8")));
    assertEquals("test2", data);
    input.close();
  }

  @Test
  public void testLoadManyDocuments() throws IOException  {
    InputStream input = new FileInputStream(new File("src/test/resource/example2_28.yaml"));
    Yaml yaml = new Yaml();
    int counter = 0;
    for ( Object data : yaml.loadAll(input) ) {
      assertNotNull(data);
      assertTrue(data.toString().length() > 1);
      counter++;
    }
    assertEquals(3, counter);
    input.close();
  }

  @Test
  public void testWriteAndRead() throws IOException {
    Map<String, Object> root = new LinkedHashMap<String, Object>();
    Map<String, Object> parent = new LinkedHashMap<String, Object>();
    Map<String, Object> child1 = new LinkedHashMap<String, Object>();
    root.put("parent", parent);
    parent.put("time", System.currentTimeMillis());
    parent.put("child1", child1);
    child1.put("path1", "/a/b/c");
    child1.put("path2", "/b/c/d");
    child1.put("path3", "/e/f/c");
    FileWriter writer = new FileWriter("src/test/resource/test.yml");
    Yaml yaml = new Yaml();
    yaml.dump(root, writer);
    FileReader reader = new FileReader("src/test/resource/test.yml");
    Object obj = yaml.load(reader);
    System.out.println(obj);
  }
}
