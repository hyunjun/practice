import java.util.Scanner;

public class Solution {
  public static void flavorIndex(final int[] flavors, final int money)  {
    for ( int i = 0; i < flavors.length - 1; ++i )  {
      for ( int j = i + 1; j < flavors.length; ++j )  {
        if ( flavors[i] + flavors[j] == money ) {
          System.out.println(String.format("%d %d", i + 1, j + 1));
          return;
        }
      }
    }
  }
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int t = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < t; ++i ) {
      final int m = Integer.parseInt(sc.nextLine());
      final int n = Integer.parseInt(sc.nextLine());
      String[] inps = sc.nextLine().split(" ");
      final int[] flavors = new int[inps.length];
      for ( int j = 0; j < flavors.length; ++j )
        flavors[j] = Integer.parseInt(inps[j]);
      flavorIndex(flavors, m);
    }
  }
}
