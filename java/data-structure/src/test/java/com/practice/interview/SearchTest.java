package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class SearchTest
{
	@Test
    public void testBinarySearch()	{
		final int[] arr	=	new int[] { 15, 21, 32, 36, 48, 54, 68 };
		for ( final int i : arr )
			assertEquals(true, Search.binarySearch(arr, i));
		assertEquals(false, Search.binarySearch(arr, 67));
    }
}
