import java.util.Scanner;

public class Solution {
  public static void insertionSort(int[] arr) {
    for ( int i = 1; i < arr.length; ++i )  {
      for ( int j = i; j > 0; --j ) {
        if ( arr[j] < arr[j - 1] )  {
          int tmp = arr[j];
          arr[j] = arr[j - 1];
          arr[j - 1] = tmp;
        }
      }
      System.out.print(arr[0]);
      for ( int j = 1; j < arr.length; ++j )  System.out.print(" " + arr[j]);
      System.out.println();
    }
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int s = Integer.parseInt(sc.nextLine());
    String[] inps = sc.nextLine().split(" ");
    int[] arr = new int[inps.length];
    for ( int i = 0; i < arr.length; ++i )
      arr[i] = Integer.parseInt(inps[i]);
    insertionSort(arr);
  }
}
