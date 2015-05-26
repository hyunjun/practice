import java.util.Scanner;
import java.util.Stack;

public class Solution {
  /*public static boolean isBalanced(final String s) {
    Stack<Character> stack = new Stack<Character>();
    int len = s.length();
    for ( int i = 0; i < len; ++i )  {
      char c = s.charAt(i);
      switch ( c )  {
        case '{':
        case '(':
        case '[':
          stack.push(c);
          break;
        case '}':
          if ( '{' == stack.peek() )
            stack.pop();
          break;
        case ')':
          if ( '(' == stack.peek() )
            stack.pop();
          break;
        case ']':
          if ( '[' == stack.peek() )
            stack.pop();
          break;
      }
    }
    if ( stack.empty() )
      return true;
    return false;
  }*/
  public static boolean isBalanced(String s)  {
    int len = s.length();
    if ( 0 == len )
      return true;
    for ( int i = 0; i < len - 1; ++i ) {
      String sub = s.substring(i, i + 2);
      if ( sub.equals("()") || sub.equals("{}") || sub.equals("[]") )
        return isBalanced(s.replace(sub, ""));
    }
    return false;
  }
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    while ( sc.hasNext() )
      System.out.println(isBalanced(sc.nextLine()));
  }
}
