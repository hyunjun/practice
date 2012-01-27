package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

public class RobotTest	{
	@Test
	public void testGetPath()	{
		assertEquals(1, Robot.getPath(1, 1));
		assertEquals(2, Robot.getPath(2, 2));
		assertEquals(6, Robot.getPath(3, 3));
	}
	@Test
	public void testPrintPath()	{
		Robot	r	=	new Robot();
		r.createTree(3, 3);
		r.printPath(3, 3);
	}
}
