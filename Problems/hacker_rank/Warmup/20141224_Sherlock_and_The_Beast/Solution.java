import java.util.Scanner;

public class Solution {
  public static String decentNumber(final int N) {
    int fiveStart = N;
    while ( 0 < fiveStart && fiveStart % 3 != 0 )
      --fiveStart;
    int threeStart = N;
    while ( 0 < threeStart && threeStart % 5 != 0 )
      --threeStart;
    for ( int f = fiveStart; f >= 0; f -= 3 ) {
      for ( int t = threeStart; t >= 0; t -= 5 )  {
        if ( f + t == N ) {
          StringBuffer sb = new StringBuffer();
          while ( 0 < f-- ) sb.append("5");
          while ( 0 < t-- ) sb.append("3");
          return sb.toString();
        }
      }
    }
    return "-1";
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int T = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < T; ++i ) {
      System.out.println(decentNumber(Integer.parseInt(sc.nextLine())));
    }
  }
}
