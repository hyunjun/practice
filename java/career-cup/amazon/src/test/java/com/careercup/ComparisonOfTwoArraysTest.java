package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

public class ComparisonOfTwoArraysTest
{
	@Test
    public void testComparisonOfTwoArrays()
	{
		ComparisonOfTwoArrays	c	=
			new ComparisonOfTwoArrays(
				new int[] { 1, 2, 4, 5, 9, 10 }, new int[] { 2, 3, 6, 9, 10 });
		c.compare();
		c.print(12);
		int[]	expected	=	new int[] { 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1 };
		int[]	result	=	new int[expected.length];
		for ( int i = 0; i < result.length; ++i )
			result[i]	=	c.res[i];
		assertArrayEquals(expected, result);
	}
}
