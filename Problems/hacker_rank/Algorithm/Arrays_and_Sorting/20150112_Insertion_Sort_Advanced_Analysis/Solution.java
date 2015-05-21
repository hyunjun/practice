import java.util.Scanner;

public class Solution {
  public static long mergeSort(int[] arr) {
    return merge(arr, 0, arr.length);
  }
  public static long merge(int[] arr, int l, int r)  {
    if ( r - l < 2 )  {
      return 0;
    }
    int i = 0;
    int m = (r + l) / 2;
    long l_cnt = merge(arr, l, m);
    long r_cnt = merge(arr, m, r);
    long cnt = l_cnt + r_cnt;
    int[] tmp = new int[r - l];
    int l_idx = l, r_idx = m, t_idx = 0;
    while ( l_idx < m && r_idx < r )  {
      if ( arr[l_idx] <= arr[r_idx] ) {
        tmp[t_idx++] = arr[l_idx++];
      } else  {
        cnt += m - l_idx;
        tmp[t_idx++] = arr[r_idx++];
      }
    }
    while ( l_idx < m ) tmp[t_idx++] = arr[l_idx++];
    while ( r_idx < r ) tmp[t_idx++] = arr[r_idx++];
    for ( i = l; i < l + t_idx; ++i ) arr[i] = tmp[i - l];
    return cnt;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int t = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < t; ++i ) {
      int n = Integer.parseInt(sc.nextLine());
      String[] inps = sc.nextLine().split(" ");
      int[] arr = new int[inps.length];
      for ( int j = 0; j < arr.length; ++j )
        arr[j] = Integer.parseInt(inps[j]);
      System.out.println(mergeSort(arr));
    }
  }
}
