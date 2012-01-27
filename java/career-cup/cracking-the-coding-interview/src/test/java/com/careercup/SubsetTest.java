package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.HashSet;
import	java.util.Iterator;
import	java.util.Set;

public class SubsetTest	{
	@Test
	public void testGetSubset()	{
		Subset	ss	=	new Subset();
		Set<Integer>	s	=	new HashSet<Integer>();
		s.add(1);
		s.add(2);
		s.add(3);
		Set<Set<Integer>>	rss	=	ss.getSubset(s);
		for ( Iterator<Set<Integer>> itr = rss.iterator(); itr.hasNext(); )
			System.out.println(itr.next());
	}
}
