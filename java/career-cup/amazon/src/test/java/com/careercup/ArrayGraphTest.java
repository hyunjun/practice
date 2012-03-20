package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.List;

public class ArrayGraphTest
{
	@Test
    public void testArrayGraph()
	{
		int[]	nodes	=	new int[]{ 1, 3, 3, -1, 3, 1 };
		assertEquals(3, ArrayGraph.getHeight(nodes));
		assertEquals(3, ArrayGraph.getHeight1(nodes));
	}
}
