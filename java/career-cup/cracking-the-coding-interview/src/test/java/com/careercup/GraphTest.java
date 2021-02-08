package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

public class GraphTest
{
	//	4.1
	@Test
    public void testHasRoute()
    {
		Graph	g	=	new Graph();
		g.addEdge(0, 1);
		g.addEdge(0, 2);
		g.addEdge(1, 3);
		assertEquals(false, g.hasRoute());
		g.addEdge(2, 3);
		assertEquals(true, g.hasRoute());
    }
}
