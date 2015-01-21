import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

public class Solution {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    sc.nextLine();
    String[] inps = sc.nextLine().split(" ");

    Map<Integer, Integer> m = new HashMap<Integer, Integer>();
    for ( String inp : inps ) {
      int i = Integer.parseInt(inp);
      if ( m.containsKey(i) ) {
        m.put(i, m.get(i) + 1);
      } else  {
        m.put(i, 1);
      }
    }
    for ( Entry<Integer, Integer> entry : m.entrySet() )  {
      if ( entry.getValue() == 1 )  {
        System.out.println(entry.getKey());
        break;
      }
    }
  }
}
