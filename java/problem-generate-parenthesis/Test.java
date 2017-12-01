//  https://github.com/hyunjun/practice/blob/master/python/problem-generate-parentheses/generate_parentheses.py
import java.util.ArrayList;
import java.util.List;

public class Test {
  public static void generateParenthesis(int numRemainingLeftPs, int numRemainingRightPs, int difference, String parentheses, List<String> outputParenthesesSet)  {
    if (difference == 0) {    // only leftP can follow
      if (numRemainingLeftPs == 0) {
        outputParenthesesSet.add(parentheses);
      } else {
        generateParenthesis(numRemainingLeftPs - 1, numRemainingRightPs, difference + 1, parentheses + "(", outputParenthesesSet);
      }
    } else { // leftP and rightP can follow
      if (numRemainingLeftPs == 0) {
        generateParenthesis(numRemainingLeftPs, numRemainingRightPs - 1, difference - 1, parentheses + ")", outputParenthesesSet);
      } else {
        generateParenthesis(numRemainingLeftPs - 1, numRemainingRightPs, difference + 1, parentheses + "(", outputParenthesesSet);
        generateParenthesis(numRemainingLeftPs, numRemainingRightPs - 1, difference - 1, parentheses + ")", outputParenthesesSet);
      }
    }
  }

  public static void main(String[] args)  {
    List<String> outputs =  new ArrayList<String>();
    generateParenthesis(3, 3, 0, "", outputs);
    for ( String o : outputs )
      System.out.println(o);
  }
}
