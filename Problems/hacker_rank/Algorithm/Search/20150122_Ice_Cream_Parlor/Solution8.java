import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Solution8 {
  public static void flavorIndex(final int[] flavor, final int money) {
    IntStream.range(0, flavor.length - 1).forEach(i ->{
      IntStream.range(i + 1, flavor.length).forEach(j ->{
        if ( flavor[i] + flavor[j] == money ) {
          System.out.println(String.format("%d %d", i + 1, j + 1));
        }
      });
    });
  }
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int t = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < t; ++i ) {
      final int m = Integer.parseInt(sc.nextLine());
      final int n = Integer.parseInt(sc.nextLine());
      int[] flavor = Arrays.asList(sc.nextLine().split(" ")).stream().mapToInt(Integer::parseInt).toArray();
      flavorIndex(flavor, m);
    }
  }
}
