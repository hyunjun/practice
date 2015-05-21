import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution8 {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    int[] ar = Arrays.asList(sc.nextLine().split(" ")).stream().mapToInt(Integer::parseInt).sorted().toArray();
    int minDiff = IntStream.range(0, ar.length - 1).map((i) -> ar[i + 1] - ar[i]).reduce(Integer.MAX_VALUE, (a, b) -> a < b ? a : b);
    System.out.println(IntStream.range(0, ar.length - 1).filter((i) -> ar[i + 1] - ar[i] == minDiff).boxed().map((j) -> String.format("%d %d", ar[j], ar[j + 1])).collect(Collectors.joining(" ")));
  }
}
