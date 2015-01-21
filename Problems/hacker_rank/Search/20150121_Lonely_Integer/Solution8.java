import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Stream;

public class Solution8 {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    sc.nextLine();
    //System.out.println(Arrays.asList(sc.nextLine().split(" ")).stream().mapToInt(Integer::parseInt).boxed().collect(Collectors.toMap(x -> x, x -> 1)));
    int[] ar = Arrays.asList(sc.nextLine().split(" ")).stream().mapToInt(Integer::parseInt).toArray();

    Map<Integer, Integer> m = new HashMap<Integer, Integer>();
    for ( int a : ar ) {
      if ( m.containsKey(a) ) {
        m.put(a, m.get(a) + 1);
      } else  {
        m.put(a, 1);
      }
    }
    m.entrySet().stream().filter(e -> e.getValue() == 1).forEach(e -> { System.out.println(e.getKey()); });
  }
}
