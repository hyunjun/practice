import java.util.Scanner;

public class Solution {
  public static int insertionSort(int[] arr) {
    int cnt = 0;
    for ( int i = 1; i < arr.length; ++i )  {
      for ( int j = i; j > 0; --j ) {
        if ( arr[j] < arr[j - 1] )  {
          int tmp = arr[j];
          arr[j] = arr[j - 1];
          arr[j - 1] = tmp;
          ++cnt;
        }
      }
    }
    return cnt;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int s = Integer.parseInt(sc.nextLine());
    String[] inps = sc.nextLine().split(" ");
    int[] arr = new int[inps.length];
    for ( int i = 0; i < arr.length; ++i )
      arr[i] = Integer.parseInt(inps[i]);
    System.out.println(insertionSort(arr));
  }
}
