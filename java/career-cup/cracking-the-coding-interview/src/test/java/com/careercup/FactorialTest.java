package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.ArrayList;
import	java.util.List;

public class FactorialTest	{
	@Test
	public void testGetFactorialList()	{
		List<List<Integer>>	list2	=	Factorial.getFactorialList(2);
		assertEquals(2, list2.size());
		for ( List<Integer> l : list2 )
			System.out.println(l);

		List<List<Integer>>	list3	=	Factorial.getFactorialList(3);
		assertEquals(6, list3.size());
		for ( List<Integer> l : list3 )
			System.out.println(l);

		List<List<Integer>>	list4	=	Factorial.getFactorialList(4);
		assertEquals(24, list4.size());
		for ( List<Integer> l : list4 )
			System.out.println(l);
	}
}
