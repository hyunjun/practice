package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.List;

public class ArrayProductTest
{
	@Test
    public void testArrayProduct()
	{
		int[]	inp	=	new int[]{ 1, 2, 3, 4, 5 };
		int[]	oup	=	new int[]{ 120, 60, 40, 30, 24 };
		assertArrayEquals(oup, ArrayProduct.getArrayProduct0(inp));
		assertArrayEquals(oup, ArrayProduct.getArrayProduct1(inp));
		assertArrayEquals(oup, ArrayProduct.getArrayProduct2(inp));
	}
}
