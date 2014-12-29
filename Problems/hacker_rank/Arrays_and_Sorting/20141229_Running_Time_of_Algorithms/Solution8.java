import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Solution8 {
  public static int insertionSort(Integer[] arr) {
    int cnt = 0;
    for ( int i = 1; i < arr.length; ++i )  {
      for ( int j = i; j > 0; --j ) {
        if ( arr[j] < arr[j - 1] )  {
          int tmp = arr[j];
          arr[j] = arr[j - 1];
          arr[j - 1] = tmp;
          ++cnt;
        }
      }
    }
    return cnt;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int s = Integer.parseInt(sc.nextLine());
    Integer[] arr = Arrays.asList(sc.nextLine().split(" ")).stream().map(i -> Integer.parseInt(i)).toArray(Integer[]::new);
    System.out.println(insertionSort(arr));
  }
}
