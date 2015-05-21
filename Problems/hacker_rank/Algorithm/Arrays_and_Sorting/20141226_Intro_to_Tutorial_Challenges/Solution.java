import java.util.Scanner;

public class Solution {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int V = Integer.parseInt(sc.nextLine());
    final int n = Integer.parseInt(sc.nextLine());
    final String[] arr = sc.nextLine().split(" ");
    for ( int i = 0; i < arr.length; ++i )  {
      if ( V == Integer.parseInt(arr[i]) )  {
        System.out.println(i);
      }
    }
  }
}
