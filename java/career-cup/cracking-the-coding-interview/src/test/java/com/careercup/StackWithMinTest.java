package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

//	3.1
public class StackWithMinTest
{
	@Test
    public void testStackWithMin()
    {
		StackWithMin	s	=	new StackWithMin(10);
		assertEquals(Integer.MIN_VALUE, s.pop());
		assertEquals(Integer.MIN_VALUE, s.min());
		s.push(4);
		assertEquals(4, s.min());
		s.push(6);
		assertEquals(4, s.min());
		s.push(10);
		assertEquals(4, s.min());
		s.push(3);
		assertEquals(3, s.min());
		s.push(9);
		assertEquals(3, s.min());
		s.push(7);
		assertEquals(3, s.min());
		s.push(2);
		assertEquals(2, s.min());
		s.push(8);
		assertEquals(2, s.min());
		s.push(1);
		assertEquals(1, s.min());
		s.push(5);
		assertEquals(1, s.min());
		s.push(0);
		assertEquals(1, s.min());

		assertEquals(5, s.pop());
		assertEquals(1, s.min());
		assertEquals(1, s.pop());
		assertEquals(2, s.min());
		assertEquals(8, s.pop());
		assertEquals(2, s.min());
		assertEquals(2, s.pop());
		assertEquals(3, s.min());
		assertEquals(7, s.pop());
		assertEquals(3, s.min());
		assertEquals(9, s.pop());
		assertEquals(3, s.min());
		assertEquals(3, s.pop());
		assertEquals(4, s.min());
		assertEquals(10, s.pop());
		assertEquals(4, s.min());
		assertEquals(6, s.pop());
		assertEquals(4, s.min());
		assertEquals(4, s.pop());
		assertEquals(Integer.MIN_VALUE, s.min());
		assertEquals(Integer.MIN_VALUE, s.pop());
    }
}
