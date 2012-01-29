package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

public class AddTest	{
	@Test
	public void testAddset()	{
		assertEquals(2, Add.add(1, 1));
		assertEquals(3, Add.add(1, 2));
		assertEquals(8, Add.add(3, 5));
		assertEquals(9, Add.add(4, 5));
		assertEquals(111, Add.add(41, 70));

		assertEquals(2, Add.add_no_arithm(1, 1));
		assertEquals(3, Add.add_no_arithm(1, 2));
		assertEquals(8, Add.add_no_arithm(3, 5));
		assertEquals(9, Add.add_no_arithm(4, 5));
		assertEquals(111, Add.add_no_arithm(41, 70));
	}
}
