import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Solution8  {
  public static String decentNumber(final int N) {
    final int fiveStart = IntStream.range(0, N + 1).filter(n -> n % 3 == 0).max().getAsInt();
    final int threeStart = IntStream.range(0, N + 1).filter(n -> n % 5 == 0).max().getAsInt();
    /*IntStream.range(0, N + 1).filter(n -> n % 3 == 0).forEach(f -> {
      IntStream.range(0, N + 1).filter(m -> m % 5 == 0).forEach(t -> {
        System.out.println(f + ", " + t);
      });
      IntStream.range(0, N + 1).filter(m -> m % 5 == 0).filter(n -> f + n == N).forEach(t -> {
        System.out.println(f + ", " + t);
      });
    });*/
    /*IntStream.iterate(N + 1, i -> i - 1).limit(N + 2).filter(n -> n % 3 == 0).forEach(f -> {
      IntStream.iterate(N + 1, i -> i - 1).limit(N + 2).filter(n -> n % 5 == 0 && f + n == N).findFirst().orElse(-1);
      if ( -1 != t )  {
        System.out.println(f + "\t" + t);
      }
    });*/
    //IntStream.iterate(N + 1, i -> i - 1).limit(N + 2).filter(n -> n % 3 == 0)
    //  .map(f -> IntStream.iterate(N + 1, j -> j - 1).limit(N + 2).filter(m -> m % 5 == 0 && f + m == N));
    /*IntStream.iterate(N + 1, i -> i - 1).limit(N + 2).filter(n -> n % 3 == 0).forEach(f -> {
      IntStream.iterate(N + 1, i -> i - 1).limit(N + 2).filter(n -> n % 5 == 0 && f + n == N).forEach(t -> {
        StringBuffer sb = new StringBuffer();
        IntStream.range(0, f).forEach(i -> {sb.append("5");});
        IntStream.range(0, t).forEach(i -> {sb.append("3");});
        System.out.println(sb.toString());
      });
    });*/
    //IntStream.iterate(N + 1, i -> i - 1).limit(N + 2).filter(n -> n % 3 == 0)
    //  .map(i -> IntStream.iterate(N + 1, i -> i - 1).limit(N + 2).filter(n -> n % 5 == 0).filter( 
    for ( int f = fiveStart; f >= 0; f -= 3 ) {
      for ( int t = threeStart; t >= 0; t -= 5 )  {
        if ( f + t == N ) {
          StringBuffer sb = new StringBuffer();
          IntStream.range(0, f).forEach(i -> {sb.append("5");});
          IntStream.range(0, t).forEach(i -> {sb.append("3");});
          return sb.toString();
        }
      }
    }
    return "-1";
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int T = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < T; ++i ) {
      System.out.println(decentNumber(Integer.parseInt(sc.nextLine())));
    }
  }
}
