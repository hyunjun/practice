import java.util.Scanner;

public class Solution {
  public static int[] countingSort(final int[] ar)  {
    int[] counts = new int[100];
    for ( int i = 0; i < ar.length; ++i )  {
      ++counts[ar[i]];
    }
    for ( int i = 1; i < 100; ++i ) {
      if ( 0 < counts[i] )  {
        counts[i] += counts[i - 1];
      } else if ( 0 == counts[i] )  {
        counts[i] = counts[i - 1];
      }
    }
    return counts;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int n = Integer.parseInt(sc.nextLine());
    int[] ar = new int[n];
    for ( int i = 0; i < n; ++i ) {
      String[] inps = sc.nextLine().split(" ");
      ar[i] = Integer.parseInt(inps[0]);
    }
    int[] res = countingSort(ar);
    System.out.print(res[0]);
    for ( int i = 1; i < res.length; ++i )  {
      System.out.print(" " + res[i]);
    }
    System.out.println();
  }
}
