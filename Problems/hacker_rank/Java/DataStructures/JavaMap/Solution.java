import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    Map<String, String> m = new HashMap<String, String>();
    for ( int i = 0; i < n; ++i ) {
      m.put(sc.nextLine(), sc.nextLine());
    }
    while ( sc.hasNext() )  {
      String key = sc.nextLine();
      if ( m.containsKey(key) )
        System.out.println(key + "=" + m.get(key));
      else
        System.out.println("Not found");
    }
  }
}
