import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution8 {
  public static void printArray(final int[] arr)  {
    System.out.println(Arrays.stream(arr, 0, arr.length).boxed().map(a -> a.toString()).collect(Collectors.joining(" ")));
  }

  public static int[] quickSort(IntStream arStream) {
    final int[] ar = arStream.toArray();
    final int pivot = ar[0];
    int[] left = IntStream.of(ar).filter(i -> i < pivot).toArray();
    if ( 1 < left.length )  {
      left = quickSort(IntStream.of(left));
      printArray(left);
    }
    int[] right = IntStream.of(ar).filter(i -> pivot < i).toArray();
    if ( 1 < right.length ) {
      right = quickSort(IntStream.of(right));
      printArray(right);
    }
    int[] res = new int[left.length + right.length + 1];
    System.arraycopy(left, 0, res, 0, left.length);
    res[left.length] = pivot;
    System.arraycopy(right, 0, res, left.length + 1, right.length);
    return res;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int n = Integer.parseInt(sc.nextLine());
    IntStream ar = Arrays.asList(sc.nextLine().split(" ")).stream().mapToInt(Integer::parseInt);
    final int[] res = quickSort(ar);
    printArray(res);
  }
}
