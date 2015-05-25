import java.util.Scanner;
import java.util.regex.*;

class myRegex  {
  String pattern = null;

  public myRegex()  {
    pattern = "([01]?\\d{1,2}|2[0-4]\\d|25[0-5])(\\.([01]?\\d{1,2}|2[0-4]\\d|25[0-5])){3}";
  }
  public static void main(final String[] args)  {
    Scanner in = new Scanner(System.in);
    while ( in.hasNext() )  {
      String ip = in.nextLine();
      System.out.println(ip + "\t" + ip.matches(new myRegex().pattern));
    }
  }
}
