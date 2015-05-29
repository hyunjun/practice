import java.util.Scanner;

public class Solution {
  public static int sum(int[][] board, int r, int c)  {
    int sum = 0;
    for ( int i = r; i < r + 3; ++i ) {
      if ( i == r + 1 )
        sum += board[i][c + 1];
      else  {
        for ( int j = c; j < c + 3; ++j ) {
          sum += board[i][j];
        }
      }
    }
    return  sum;
  }
  public static void main(String[] args)  {
    Scanner sc = new Scanner(System.in);
    int[][] board = new int[6][6];
    for ( int i = 0; i < 6; ++i ) {
      String[] inps = sc.nextLine().split(" ");
      for ( int j = 0; j < 6; ++j ) {
        board[i][j] = Integer.parseInt(inps[j]);
      }
    }
    int max = Integer.MIN_VALUE;
    for ( int i = 0; i < 4; ++i ) {
      for ( int j = 0; j < 4; ++j ) {
        int curMax = sum(board, i, j);
        //System.out.println(String.format("[%d][%d] %d", i, j, curMax));
        max = Math.max(max, curMax);
      }
    }
    System.out.println(max);
  }
}
