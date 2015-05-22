import java.util.Scanner;

public class Loop {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int t = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < t; ++i ) {
      String[] inps = sc.nextLine().split(" ");
      int a = Integer.parseInt(inps[0]);
      int b = Integer.parseInt(inps[1]);
      int n = Integer.parseInt(inps[2]);
      int s = a + (int) Math.pow(2, 0) * b;
      System.out.print(s);
      for ( int j = 1; j < n; ++j )  {
        s += Math.pow(2, j) * b;
        System.out.print(" " + s);
      }
      System.out.println();
    }
  }
}
