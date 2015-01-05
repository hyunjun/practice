import java.util.Scanner;

public class Solution {
  public static int[] countingSort(final int[] ar)  {
    int[] res = new int[100];
    for ( int i = 0; i < ar.length; ++i )  {
      ++res[ar[i]];
    }
    return res;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int n = Integer.parseInt(sc.nextLine());
    String[] inps = sc.nextLine().split(" ");
    int[] ar = new int[inps.length];
    for ( int i = 0; i < ar.length; ++i )
      ar[i] = Integer.parseInt(inps[i]);
    int[] res = countingSort(ar);
    System.out.print(res[0]);
    for ( int i = 1; i < res.length; ++i )  {
      System.out.print(" " + res[i]);
    }
    System.out.println();
  }
}
