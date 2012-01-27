package com.practice.interview;

import	java.util.ArrayList;
import	java.util.Enumeration;
import	java.util.Iterator;

public class Adapter 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}

//	http://iilii.egloos.com/3789009
class IteratorToEnumeration implements Enumeration<String>	{
	private Iterator<String>	iter;
	public IteratorToEnumeration(Iterator<String> iter)	{
		this.iter	=	iter;
	}
	public boolean hasMoreElements()	{
		return	iter.hasNext();
	}
	public String nextElement()	{
		return	iter.next();
	}
}
