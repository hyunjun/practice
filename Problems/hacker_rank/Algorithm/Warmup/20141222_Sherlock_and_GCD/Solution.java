import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Solution  {
  public static boolean hasSubset(final int[] arr)  {
    int i = 2;
    int maxNum = 0;
    for ( Integer a : arr ) {
      if ( maxNum < a )
        maxNum = a;
    }
    Set<Integer> noSet = new HashSet<Integer>();
    noSet.add(0);

    Set<Integer> primeSet = new HashSet<Integer>();
    while ( i < maxNum + 1 )  {
      primeSet.clear();
      for ( Integer a : arr ) {
        primeSet.add(a % i);
      }
      if ( primeSet.equals(noSet) )
        return false;
      ++i;
    }
    return true;
  }
  public static void main(String[] args)  {
    Scanner sc = new Scanner(System.in);
    int T = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < T; ++i ) {
      int N = Integer.parseInt(sc.nextLine());
      String[] inp = sc.nextLine().split(" ");
      int[] arr = new int[inp.length];
      for ( int j = 0; j < inp.length; ++j )  {
        arr[j] = Integer.parseInt(inp[j]);
      }
      if ( hasSubset(arr) )
        System.out.println("YES");
      else
        System.out.println("NO");
    }
  }
}
