import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Collections;

public class Solution {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    int k = Integer.parseInt(sc.nextLine());
    List<String> l = new ArrayList<String>();
    for ( int i = 0; i <= s.length() - k; ++i )
      l.add(s.substring(i, i + k));
    Collections.sort(l);
    System.out.println(l.get(0));
    System.out.println(l.get(l.size() - 1));
  }
}
