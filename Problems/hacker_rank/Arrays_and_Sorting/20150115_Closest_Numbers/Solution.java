import java.util.Arrays;
import java.util.Scanner;

public class Solution {
  public static int getMinDiff(final int[] ar)  {
    int min = Integer.MAX_VALUE;
    for ( int i = 0; i < ar.length - 1; ++i ) {
      if ( ar[i + 1] - ar[i] < min )  {
        min = ar[i + 1] - ar[i];
      }
    }
    return min;
  }
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    int[] ar = new int[n];
    String[] inps = sc.nextLine().split(" ");
    for ( int i = 0; i < ar.length; ++i )
      ar[i] = Integer.parseInt(inps[i]);
    Arrays.sort(ar);
    int[] res = new int[2 * (n - 1)];
    int rIdx = 0;
    final int minDiff = getMinDiff(ar);
    for ( int i = 0; i < ar.length - 1; ++i ) {
      if ( ar[i + 1] - ar[i] == minDiff ) {
        res[rIdx++] = ar[i];
        res[rIdx++] = ar[i + 1];
      }
    }
    System.out.print(res[0]);
    for ( int i = 1; i < rIdx; ++i )  System.out.print(" " + res[i]);
    System.out.println();
  }
}
