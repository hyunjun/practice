package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

//	3.6
public class StackSortTest
{
	@Test
    public void testStackSort()
    {
		StackSort	s	=	new StackSort(5);
		s.push(10);
		s.push(40);
		s.push(50);
		s.push(20);
		s.push(30);
		System.out.println(s);
		s.sort();
		System.out.println(s);
    }
}
