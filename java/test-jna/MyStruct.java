import com.sun.jna.Structure;
import com.sun.jna.Pointer;

import java.util.Arrays;
import java.util.List;

public class MyStruct extends Structure implements Structure.ByReference {
  public int a;
  public int b;

  public MyStruct() {
  }

  public MyStruct(Pointer p) {
    super(p);
    read();
  }

  //  Without overriding getFieldOrder(), the error below occurs
  //  error: MyStruct is not abstract and does not override abstract method getFieldOrder() in Structure
  @Override
  protected List getFieldOrder() {
    //  http://stackoverflow.com/questions/15050391/how-to-make-structure-in-jna
    return Arrays.asList(new String[]{"a", "b"});
  }
}
