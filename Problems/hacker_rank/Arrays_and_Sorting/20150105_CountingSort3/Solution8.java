import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution8 {
  public static int[] countingSort(final int[] ar) {
    int[] counts = new int[100];
    for ( int i = 0; i < ar.length; ++i )  {
      ++counts[ar[i]];
    }
    for ( int i = 1; i < 100; ++i ) {
      if ( 0 < counts[i] ) {
        counts[i] += counts[i - 1];
      } else if ( 0 == counts[i] )  {
        counts[i] = counts[i - 1];
      }
    }
    return counts;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int n = Integer.parseInt(sc.nextLine());
    int[] ar = new int[n];
    for ( int i = 0; i < n; ++i ) {
      ar[i] = Integer.parseInt(sc.nextLine().split(" ")[0]);
    }
    final int[] res = countingSort(ar);
    System.out.println(Arrays.stream(res, 0, res.length).boxed().map(a -> a.toString()).collect(Collectors.joining(" ")));
  }
}
