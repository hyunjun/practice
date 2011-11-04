package com.knoa.practice;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.print("Hello World!");
		for ( String arg : args )
			System.out.print("\t" + arg);
        System.out.println();
    }
}
