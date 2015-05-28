import java.util.Scanner;

public class Solution {
  public static boolean move(int[] arr, int j, int m)  {
    if ( arr.length <= j + m )  {
      return true;
    }
    arr[j] = 1;
    boolean hasEscaped = false;
    if ( j + m < arr.length && 0 == arr[j + m] )  {
      hasEscaped = move(arr, j + m, m);
    }
    if ( false == hasEscaped && j + 1 < arr.length && 0 == arr[j + 1] )  {
      hasEscaped = move(arr, j + 1, m);
    }
    if ( false == hasEscaped && 0 <= j - 1 && 0 == arr[j - 1] )  {
      hasEscaped = move(arr, j - 1, m);
    }
    return  hasEscaped;
  }
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int T = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < T; ++i ) {
      String[] firsts = sc.nextLine().split(" ");
      int n = Integer.parseInt(firsts[0]);
      int m = Integer.parseInt(firsts[1]);
      String[] seconds = sc.nextLine().split(" ");
      int[] arr = new int[n];
      //System.out.println(n + " " + m);
      for ( int j = 0; j < n; ++j ) {
        arr[j] = Integer.parseInt(seconds[j]);
        //System.out.println("[" + j + "] " + arr[j]);
      }
      if ( move(arr, 0, m) )
        System.out.println("YES");
      else
        System.out.println("NO");

      /*int j = 0;
      while ( true ) {
        if ( n <= j + m ) {
          System.out.println("YES");
          break;
        } else if ( j + m < n && 0 == arr[j + m] ) {
          j += m;
        } else if ( j + 1 < n && 0 == arr[j + 1] )  {
          ++j;
        } else if ( 0 <= j - 1 && 0 == arr[j - 1] )  {
          --j;
        } else  {
          System.out.println("NO");
          break;
        }
        arr[j] = -1;
      }*/
    }
  }
}
