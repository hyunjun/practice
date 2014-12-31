import java.util.Scanner;

public class Solution {
  public static void printArray(final int[] arr)  {
    System.out.print(arr[0]);
    for ( int i = 1; i < arr.length; ++i )  System.out.print(" " + arr[i]);
    System.out.println();
  }

  public static int[] quickSort(final int[] ar) {
    int pivot = ar[0];
    int idx = 0;
    int l_size = 0;
    for ( int i = 0; i < ar.length; ++i )  {
      if ( ar[i] < pivot )  {
        ++l_size;
      }
    }
    int[] left = new int[l_size];
    idx = 0;
    for ( int i = 0; i < ar.length; ++i )  {
      if ( ar[i] < pivot )  {
        left[idx++] = ar[i];
      }
    }
    if ( 1 < l_size ) {
      left = quickSort(left);
      printArray(left);
    }
    int r_size = 0;
    for ( int i = 0; i < ar.length; ++i )  {
      if ( pivot < ar[i] )  {
        ++r_size;
      }
    }
    int[] right = new int[r_size];
    idx = 0;
    for ( int i = 0; i < ar.length; ++i ) {
      if ( pivot < ar[i] )  {
        right[idx++] = ar[i];
      }
    }
    if ( 1 < r_size ) {
      right = quickSort(right);
      printArray(right);
    }
    int[] res = new int[ar.length];
    idx = 0;
    System.arraycopy(left, 0, res, idx, l_size);
    idx += l_size;
    res[idx++] = pivot;
    System.arraycopy(right, 0, res, idx, r_size);
    return res;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int n = Integer.parseInt(sc.nextLine());
    final String[] inps = sc.nextLine().split(" ");
    final int[] ar = new int[inps.length];
    for ( int i = 0; i < ar.length; ++i ) ar[i] = Integer.parseInt(inps[i]);
    final int[] res = quickSort(ar);
    printArray(res);
  }
}
