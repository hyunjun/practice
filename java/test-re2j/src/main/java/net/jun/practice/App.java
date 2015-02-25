package net.jun.practice;

import com.google.re2j.*;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        final String[] pattern = { "ab+c", "한.*국" };
        final String[] matching = { "abbbc", "한민국" };
        final String[] nonMatching = { "ac", "한국가" };
        for ( int i = 0; i < pattern.length; ++i )  {
          System.out.println(String.format("\npattern %s", pattern[i]));
          Pattern p = Pattern.compile(pattern[i]);
          System.out.println(String.format("matching with %s = %b %b", matching[i], Pattern.matches(pattern[i], matching[i]), p.matcher(matching[i]).matches()));
          System.out.println(String.format("matching with %s = %b %b", nonMatching[i], Pattern.matches(pattern[i], nonMatching[i]), p.matcher(nonMatching[i]).matches()));
        }
    }
}
