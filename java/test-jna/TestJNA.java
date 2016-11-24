import com.sun.jna.Library;
import com.sun.jna.Native;

public class TestJNA  {
  public interface CLibrary extends Library {
    int getpid();
    int getppid();
    long time(long buf[]);

    public void exampleMethod(String val);
    public int example_of_add_strlen(String s1, String s2);
    public int example_of_int(int a, int b);
    public float example_of_float(float a, float b);
  }

  public static void main(String[] args)  {
    CLibrary mylib = (CLibrary)Native.loadLibrary("test", CLibrary.class);

    //  C standard library
    System.out.println("getpid()\t" + mylib.getpid());
    System.out.println("getppid()\t" + mylib.getppid());
    long[] timenul = new long[1];
    System.out.println("time()\t" + mylib.time(timenul));

    //  custom function
    mylib.exampleMethod("ImAString");
    System.out.println(mylib.example_of_add_strlen("str1", "string2"));
    System.out.println(mylib.example_of_add_strlen("", "string2"));
    System.out.println(mylib.example_of_add_strlen("str1", null));
    System.out.println(mylib.example_of_int(2, 3));
    System.out.println(mylib.example_of_float((float) 2.1, (float) 3.2));
  }
}
