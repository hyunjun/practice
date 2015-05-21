import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution8 {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    int[] ar = Arrays.asList(sc.nextLine().split(" ")).stream().mapToInt(Integer::parseInt).sorted().toArray();
    System.out.println(ar[n / 2]);
  }
}
