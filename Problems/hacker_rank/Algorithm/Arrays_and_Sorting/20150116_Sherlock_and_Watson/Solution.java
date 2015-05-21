import java.util.Scanner;

public class Solution {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    String[] inps = sc.nextLine().split(" ");
    final int N = Integer.parseInt(inps[0]);
    final int K = Integer.parseInt(inps[1]) % N;
    final int Q = Integer.parseInt(inps[2]);
    inps = sc.nextLine().split(" ");
    int[] ar = new int[inps.length];
    for ( int i = 0; i < ar.length; ++i )
      ar[i] = Integer.parseInt(inps[i]);
    int[] tmp = new int[K];
    int idx = N - K;
    System.arraycopy(ar, idx, tmp, 0, K);
    System.arraycopy(ar, 0, ar, N - idx, N - K);
    System.arraycopy(tmp, 0, ar, 0, K);
    for ( int i = 0; i < Q; ++i ) {
      int q = Integer.parseInt(sc.nextLine());
      System.out.println(ar[q]);
    }
  }
}
