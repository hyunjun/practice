import java.util.Arrays;
import java.util.Scanner;

public class Solution {
  public static boolean hasSameContents(int[] ar1, int[] ar2) {
    if ( ar1.length != ar2.length )
      return false;
    for ( int i = 0; i < ar1.length; ++i )
      if ( ar1[i] != ar2[i] )
        return false;
    return true;
  }

  public static void isPosiibleToSort(int[] ar) {
    int[] sorted = new int[ar.length];
    System.arraycopy(ar, 0, sorted, 0, ar.length);
    Arrays.sort(sorted);

    int l = 0, r = ar.length - 1;
    while ( l < r && ar[l] < ar[l + 1] )  ++l;
    while ( 0 < r && ar[r - 1] < ar[r] )  --r;

    int tmp = ar[l];
    ar[l] = ar[r];
    ar[r] = tmp;
    if ( hasSameContents(ar, sorted) )  {
      System.out.println(String.format("yes\nswap %d %d", l + 1, r + 1));
      return;
    }
    int lTmp = l + 1, rTmp = r - 1;
    while ( lTmp < rTmp ) {
      tmp = ar[lTmp];
      ar[lTmp++] = ar[rTmp];
      ar[rTmp--] = tmp;
    }
    if ( hasSameContents(ar, sorted) )  {
      System.out.println(String.format("yes\nreverse %d %d", l + 1, r + 1));
    } else  {
      System.out.println("no");
    }
  }
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    String[] inps = sc.nextLine().split(" ");
    int[] ar = new int[inps.length];
    for ( int i = 0; i < ar.length; ++i )
      ar[i] = Integer.parseInt(inps[i]);
    isPosiibleToSort(ar);
  }
}
