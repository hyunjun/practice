import java.util.Scanner;

public class Solution {
  public static void printArr(final int[] arr)  {
    System.out.print(arr[0]);
    for ( int i = 1; i < arr.length; ++i )  {
      System.out.print(" " + arr[i]);
    }
    System.out.println();
  }

  public static void insertionSort(final int[] arr) {
    int V = arr[arr.length - 1];
    int idx = arr.length - 2;
    while ( -1 < idx && V < arr[idx] )  {
      arr[idx + 1] = arr[idx];
      printArr(arr);
      --idx;
    }
    arr[idx + 1] = V;
    printArr(arr);
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int s = Integer.parseInt(sc.nextLine());
    String[] inps = sc.nextLine().split(" ");
    int[] arr = new int[inps.length];
    for ( int i = 0; i < inps.length; ++i )
      arr[i] = Integer.parseInt(inps[i]);
    insertionSort(arr);
  }
}
