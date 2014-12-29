import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Solution8 {
  public static void insertionSort(Integer[] arr) {
    int V = arr[arr.length - 1];
    int idx = arr.length - 2;
    while ( -1 < idx && V < arr[idx] )  {
      arr[idx + 1] = arr[idx];
      System.out.println(Arrays.asList(arr).stream().map(i -> i.toString()).collect(Collectors.joining(" ")));
      --idx;
    }
    arr[idx + 1] = V;
    System.out.println(Arrays.asList(arr).stream().map(i -> i.toString()).collect(Collectors.joining(" ")));
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int s = Integer.parseInt(sc.nextLine());
    Integer[] arr = Arrays.asList(sc.nextLine().split(" ")).stream().map(i -> Integer.parseInt(i)).toArray(Integer[]::new);
    insertionSort(arr);
  }
}
