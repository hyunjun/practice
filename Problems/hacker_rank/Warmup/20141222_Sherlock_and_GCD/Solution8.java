import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Solution8  {
  public static boolean hasSubset(final List<Integer> arr)  {
    final int maxNum = arr.stream().reduce((i, j) -> i < j ? j : i).get();
    Set<Integer> noSet = new HashSet<Integer>(0);
    noSet.add(0);

    for ( final Integer i : Stream.iterate(2, n -> n + 1).limit(maxNum).toArray(Integer[]::new) ) {
      if ( arr.stream().map(j -> j % i).collect(Collectors.toSet()).equals(noSet) )
        return false;
    }
    return true;
  }

  public static void main(String[] args)  {
    Scanner sc = new Scanner(System.in);
    int T = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < T; ++i ) {
      int N = Integer.parseInt(sc.nextLine());
      final List<Integer> arr = new ArrayList<Integer>();
      for ( final String s : sc.nextLine().split(" ") )
        arr.add(Integer.parseInt(s));
      if ( hasSubset(arr) )
        System.out.println("YES");
      else
        System.out.println("NO");
    }
  }
}
