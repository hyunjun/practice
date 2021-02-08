package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

public class FibonacciTest
{
	@Test
	public void testRecur()	{
		assertEquals(0, Fibonacci.recur(0));
		assertEquals(1, Fibonacci.recur(1));
		assertEquals(1, Fibonacci.recur(2));
		assertEquals(2, Fibonacci.recur(3));
		assertEquals(3, Fibonacci.recur(4));
		assertEquals(5, Fibonacci.recur(5));
	}
	@Test
	public void testIter()	{
		assertEquals(0, Fibonacci.iter(0));
		assertEquals(1, Fibonacci.iter(1));
		assertEquals(1, Fibonacci.iter(2));
		assertEquals(2, Fibonacci.iter(3));
		assertEquals(3, Fibonacci.iter(4));
		assertEquals(5, Fibonacci.iter(5));
	}
}
