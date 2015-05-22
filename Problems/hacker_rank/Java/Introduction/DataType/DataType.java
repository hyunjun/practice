import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class DataType  {
  public static void main(final String[] args)  {
    Scanner sc = new Scanner(System.in);
    final int T = Integer.parseInt(sc.nextLine());
    for ( int i = 0; i < T; ++i ) {
      //System.out.println(Integer.parseInt(sc.nextLine()));
      String inp = sc.nextLine();
      List<String> dataTypes = new ArrayList<String>();
      try {
        Byte.parseByte(inp);
        dataTypes.add("* byte");
      } catch (NumberFormatException e) {
      }
      try {
        Short.parseShort(inp);
        dataTypes.add("* short");
      } catch (NumberFormatException e) {
      }
      try {
        Integer.parseInt(inp);
        dataTypes.add("* int");
      } catch (NumberFormatException e) {
      }
      try {
        Long.parseLong(inp);
        dataTypes.add("* long");
      } catch (NumberFormatException e) {
      }
      if ( 0 < dataTypes.size() ) {
        System.out.println(String.format("%s can be fitted in:", inp));
        for ( String dataType : dataTypes )
          System.out.println(dataType);
      } else  {
        System.out.println(String.format("%s can't be fitted anywhere.", inp));
      }
    }
  }
}
