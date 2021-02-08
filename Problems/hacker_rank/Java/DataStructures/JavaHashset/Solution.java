import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Solution {
  public static void main(String[] args)  {
    Scanner sc = new Scanner(System.in);
    int T = Integer.parseInt(sc.nextLine());
    Set<String> s = new HashSet<String>();
    for ( int i = 0; i < T; ++i ) {
      s.add(sc.nextLine());
      System.out.println(s.size());
    }
  }
}
