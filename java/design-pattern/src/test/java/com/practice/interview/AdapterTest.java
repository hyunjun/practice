package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.ArrayList;
import	java.util.Enumeration;
import	java.util.List;

public class AdapterTest
{
	public static void goodMethod(Enumeration<String> e)	{
		while ( e.hasMoreElements() )	{
			System.out.println(e.nextElement());
		}
	}

	@Test
    public void testAdapter()
    {
		List<String>	list	=	new ArrayList<String>();
		list.add("A");
		list.add("B");
		list.add("C");
		Enumeration<String>	ite	=	new IteratorToEnumeration(list.iterator());
		AdapterTest.goodMethod(ite);
    }
}
