import java.util.Arrays;
import java.util.Scanner;

public class Solution {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    int[] ar = new int[n];
    String[] inps = sc.nextLine().split(" ");
    for ( int i = 0; i < ar.length; ++i )
      ar[i] = Integer.parseInt(inps[i]);
    Arrays.sort(ar);
    System.out.println(ar[n / 2]);
  }
}
