import java.util.ArrayList;
import java.util.Map;
import java.util.Map.Entry;
import java.util.List;
import java.util.Scanner;
import java.util.TreeMap;

public class Solution {
  public static String countingSort(final int[] xs, final String[] ss)  {
    Map<Integer, List<String>> resMap = new TreeMap<Integer, List<String>>();
    for ( int i = 0; i < xs.length; ++i ) {
      List<String> partials = resMap.get(xs[i]);
      if ( resMap.containsKey(xs[i]) )
        partials = resMap.get(xs[i]);
      else
        partials = new ArrayList<String>();
      partials.add(ss[i]);
      resMap.put(xs[i], partials);
    }
    StringBuffer sb = new StringBuffer();
    for ( Entry<Integer, List<String>> e : resMap.entrySet() ) {
      for ( String s : e.getValue() ) {
        sb.append(" ");
        sb.append(s);
      }
    }
    return sb.toString().trim();
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int n = Integer.parseInt(sc.nextLine());
    int[] xs = new int[n];
    String[] ss = new String[n];
    for ( int i = 0; i < n; ++i ) {
      String[] inps = sc.nextLine().split(" ");
      xs[i] = Integer.parseInt(inps[0]);
      if ( i < n / 2 )
        ss[i] = "-";
      else
        ss[i] = inps[1];
    }
    System.out.println(countingSort(xs, ss));
  }
}
