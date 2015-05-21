import java.util.Scanner;

public class Solution {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int t = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < t; ++i ) {
      String[] inps = sc.nextLine().split(" ");
      final int r = Integer.parseInt(inps[0]);
      final int k = Integer.parseInt(inps[1]);
      final double radius = Math.sqrt(r);
      int cnt = 0;
      for ( int x = 0; x < radius; ++x )  {
        double dy = Math.sqrt(r - x * x);
        int y = (int) dy;
        if ( y - dy == 0 )  {
          cnt += 4;
        }
      }
      System.out.println((cnt <= k ? "" : "im") + "possible");
    }
  }
}
