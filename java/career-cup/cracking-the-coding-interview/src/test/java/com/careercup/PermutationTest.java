package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.List;

public class PermutationTest	{
	@Test
	public void testGetStrPerm()	{
		Permutation	p	=	new Permutation();
		List<String>	list	=	p.getStrPerm("abc");
		for ( String s : list )	System.out.println(s);
	}
}
