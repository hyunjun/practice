import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution8 {
  /*public static Integer[] partition(Integer[] ar) {
    Integer[] res = new Integer[ar.length];
    Integer[] left = Arrays.asList(ar).stream().filter(i -> i < ar[0]).toArray(Integer[]::new);
    Integer[] right = Arrays.asList(ar).stream().filter(i -> ar[0] < i).toArray(Integer[]::new);
    System.arraycopy(left, 0, res, 0, left.length);
    res[left.length] = ar[0];
    System.arraycopy(right, 0, res, left.length + 1, right.length);
    return res;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    Integer[] ar = Arrays.asList(sc.nextLine().split(" ")).stream().map(i -> Integer.parseInt(i)).toArray(Integer[]::new);
    Integer[] res = partition(ar);
    System.out.println(Arrays.asList(res).stream().map(a -> a.toString()).collect(Collectors.joining(" ")));
  }*/

  public static int[] partition(IntStream arStream) {
    final int[] ar = arStream.toArray();
    final int pivot = ar[0];
    int[] left = IntStream.of(ar).filter(i -> i < pivot).toArray();
    int[] right = IntStream.of(ar).filter(i -> pivot < i).toArray();
    int[] res = new int[left.length + right.length + 1];
    System.arraycopy(left, 0, res, 0, left.length);
    res[left.length] = pivot;
    System.arraycopy(right, 0, res, left.length + 1, right.length);
    return res;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    IntStream ar = Arrays.asList(sc.nextLine().split(" ")).stream().mapToInt(Integer::parseInt);
    int[] res = partition(ar);
    System.out.println(Arrays.stream(res, 0, res.length).boxed().map(a -> a.toString()).collect(Collectors.joining(" ")));
  }
}
