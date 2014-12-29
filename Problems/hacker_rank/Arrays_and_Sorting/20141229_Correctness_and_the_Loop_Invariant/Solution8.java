import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Solution8 {
  public static void insertionSort(Integer[] arr) {
    for ( int i = 1; i < arr.length; ++i )  {
      for ( int j = i; j > 0; --j ) {
        if ( arr[j] < arr[j - 1] )  {
          int tmp = arr[j];
          arr[j] = arr[j - 1];
          arr[j - 1] = tmp;
        }
      }
    }
    System.out.println(Arrays.asList(arr).stream().map(a -> a.toString()).collect(Collectors.joining(" ")));
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int s = Integer.parseInt(sc.nextLine());
    Integer[] arr = Arrays.asList(sc.nextLine().split(" ")).stream().map(i -> Integer.parseInt(i)).toArray(Integer[]::new);
    insertionSort(arr);
  }
}
