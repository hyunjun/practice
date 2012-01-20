package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class StackTest
{
	@Test
    public void testStack()
    {
		Stack	s	=	new Stack(5);
		s.push(1);
		s.print();
		s.push(2);
		s.print();
		s.push(3);
		s.print();
		s.push(4);
		s.print();
		s.push(5);
		s.print();
		s.push(5);
		s.print();
		s.push(5);
		s.print();
		assertEquals(5, s.pop());
		s.print();
		assertEquals(4, s.pop());
		s.print();
		assertEquals(3, s.pop());
		s.print();
		assertEquals(2, s.pop());
		s.print();
		assertEquals(1, s.pop());
		s.print();
		assertEquals(-1, s.pop());
		s.print();
    }
}
