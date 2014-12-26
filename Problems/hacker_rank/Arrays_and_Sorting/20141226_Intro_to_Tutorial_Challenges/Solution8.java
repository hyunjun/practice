import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.stream.Stream;

public class Solution8 {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int V = Integer.parseInt(sc.nextLine());
    final int n = Integer.parseInt(sc.nextLine());
    final Stream<String> arrStream = Pattern.compile("\\s+").splitAsStream(sc.nextLine());
    final Integer[] arr = arrStream.map(i -> Integer.parseInt(i)).toArray(Integer[]::new);
    for ( int i = 0; i < arr.length; ++i )  {
      if ( V == arr[i] )  {
        System.out.println(i);
      }
    }
  }
}
