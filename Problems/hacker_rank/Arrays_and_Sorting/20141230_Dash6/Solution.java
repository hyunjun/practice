import java.util.Scanner;

public class Solution {
  public static int[] partition(int[] ar) {
    int[] res = new int[ar.length];
    int idx = 0;
    for ( int i = 0; i < ar.length; ++i ) {
      if ( ar[i] < ar[0] )  {
        res[idx++] = ar[i];
      }
    }
    res[idx++] = ar[0];
    for ( int i = 0; i < ar.length; ++i ) {
      if ( ar[0] < ar[i] )  {
        res[idx++] = ar[i];
      }
    }
    return res;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    String[] inps = sc.nextLine().split(" ");
    int[] ar = new int[inps.length];
    for ( int i = 0; i < ar.length; ++i ) {
      ar[i] = Integer.parseInt(inps[i]);
    }
    int[] res = partition(ar);
    System.out.print(res[0]);
    for ( int i = 1; i < res.length; ++i )
      System.out.print(" " + res[i]);
    System.out.println();
  }
}
