import java.util.regex.Pattern;

//  http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/
public class Prime  {
  public static boolean isPrime(int c)  {
    String s = "";
    while ( c > 0 ) {
      c--;
      s+="1";
    }
    return  !Pattern.matches("^1?$|^(11+?)\\1+$", s);
  }

  public static void main(String[] args){
    if (args.length >= 1) {
      int c = Integer.parseInt(args[0]);
      System.out.println(c + "\t" + isPrime(c));
    }
  }
}
