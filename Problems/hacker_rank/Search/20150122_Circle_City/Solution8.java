import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Solution8 {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int t = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < t; ++i ) {
      int[] ar = Arrays.asList(sc.nextLine().split(" ")).stream().mapToInt(Integer::parseInt).toArray();
      final int r = ar[0];
      final int k = ar[1];
      final double radius = Math.sqrt(r);
      final int end = radius - (int) radius == 0 ? (int) radius : (int) radius + 1;
      if ( 4 * IntStream.range(0, end).mapToDouble(x -> Math.sqrt(r - x * x)).filter(y -> y - (int) y == 0).count() <= k )
        System.out.println("possible");
      else
        System.out.println("impossible");
    }
  }
}
