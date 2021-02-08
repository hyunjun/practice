package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

//	3.1
public class SetOfStackTest
{
	@Test
    public void testSetOfStack()
    {
		SetOfStack	s	=	new SetOfStack(4, 5);
		assertEquals(Integer.MIN_VALUE, s.pop());
		s.push(1);
		s.push(2);
		s.push(3);
		s.push(4);
		s.push(5);
		s.push(10);
		s.push(20);
		s.push(30);
		s.push(40);
		s.push(50);
		s.push(100);
		s.push(200);
		s.push(300);
		s.push(400);
		s.push(500);
		s.push(1000);
		s.push(2000);
		s.push(3000);
		s.push(4000);
		s.push(5000);

		assertEquals(5, s.popAt(0));
		assertEquals(50, s.popAt(1));
		assertEquals(500, s.popAt(2));
		assertEquals(5000, s.pop());
		//assertEquals(Integer.MIN_VALUE, s.pop());
		s.push(6);
		s.push(60);
		s.push(600);
		s.push(6000);
    }
}
