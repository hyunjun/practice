import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution8 {
  public static int[] countingSort(IntStream arStream) {
    final int[] ar = arStream.toArray();
    int[] counts = new int[100];
    for ( int i = 0; i < ar.length; ++i )  {
      ++counts[ar[i]];
    }
    int idx = 0;
    int[] res = new int[100];
    for ( int i = 0; i < counts.length; ++i ) {
      int c = counts[i];
      while ( 0 < c-- ) {
        res[idx++] = i;
      }
    }
    return res;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int n = Integer.parseInt(sc.nextLine());
    IntStream ar = Arrays.asList(sc.nextLine().split(" ")).stream().mapToInt(Integer::parseInt);
    final int[] res = countingSort(ar);
    System.out.println(Arrays.stream(res, 0, res.length).boxed().map(a -> a.toString()).collect(Collectors.joining(" ")));
  }
}
