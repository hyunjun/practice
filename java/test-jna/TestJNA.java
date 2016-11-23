import com.sun.jna.Library;
import com.sun.jna.Native;

public class TestJNA  {
  public interface CLibrary extends Library {
    public void exampleMethod(String val);
  }

  public static void main(String[] args)  {
    CLibrary mylib = (CLibrary)Native.loadLibrary("test", CLibrary.class);
    mylib.exampleMethod("ImAString");
  }
}
