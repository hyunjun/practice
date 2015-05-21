import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

public class Solution {
  private static int MAX_CNT = 1000000;
  /*public static long numOfPairs(final int[] ar)  {
    Map<Integer, Integer> cntMap = new HashMap<Integer, Integer>();
    for ( int i = 0; i < ar.length; ++i ) {
      for ( Entry<Integer, Integer> entry : cntMap.entrySet() ) {
        System.out.print("\t" + entry.getKey() + " : " + entry.getValue());
      }
      System.out.println();
      int key = ar[i];
      System.out.print("key\t" + key);
      if ( cntMap.containsKey(key) )  {
        System.out.print("\tvalue\t" + cntMap.get(i));
        cntMap.put(key, cntMap.get(i) + 1);
        System.out.println(" -> " + cntMap.get(i));
      } else  {
        cntMap.put(key, 1);
        System.out.println("\tnew value\t1");
      }
    }
    long cnt = 0;
    for ( Entry<Integer, Integer> entry : cntMap.entrySet() ) {
      int v = entry.getValue();
      if ( 1 < v )
        cnt += v * (v - 1);
    }
    return cnt;
  }*/
  public static long numOfPairs(final int[] ar) {
    long cnt = 0;
    int[] cnts = new int[MAX_CNT];
    for ( int i = 0; i < ar.length; ++i ) {
      ++cnts[ar[i] - 1];
    }
    for ( int i = 0; i < MAX_CNT; ++i ) {
      if ( 1 < cnts[i] ) {
        cnt += ((long) cnts[i]) * (cnts[i] - 1);
      }
    }
    return cnt;
  }

  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    int T = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < T; ++i ) {
      sc.nextLine();
      String[] inps = sc.nextLine().split(" ");
      int[] ar = new int[inps.length];
      for ( int j = 0; j < ar.length; ++j ) {
        ar[j] = Integer.parseInt(inps[j]);
      }
      System.out.println(numOfPairs(ar));
    }
  }
}
