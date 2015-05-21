import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution8 {
  private static int MAX_CNT = 1000000;
  public static long numOfPairs(final int[] ar) {
    long cnt = 0;
    int[] cnts = new int[MAX_CNT];
    for ( int i = 0; i < ar.length; ++i ) {
      ++cnts[ar[i] - 1];
    }
    for ( int i = 0; i < MAX_CNT; ++i ) {
      if ( 1 < cnts[i] ) {
        cnt += ((long) cnts[i]) * (cnts[i] - 1);
      }
    }
    return cnt;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int T = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < T; ++i ) {
      int n = Integer.parseInt(sc.nextLine());
      int[] ar = Arrays.asList(sc.nextLine().split(" ")).stream().mapToInt(Integer::parseInt).sorted().toArray();
      System.out.println(numOfPairs(ar));
    }
  }
}
