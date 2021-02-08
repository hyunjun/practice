package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

//	3.1
public class ArrayToThreeStacksTest
{
	@Test
    public void testArrayToThreeStacks()
    {
		ArrayToThreeStacks	s	=	new ArrayToThreeStacks(12);
		s.push(0, 1);
		s.push(0, 2);
		s.push(1, 10);
		s.push(2, 100);
		s.push(0, 3);
		s.push(1, 20);
		s.push(1, 30);
		s.push(2, 200);
		s.push(0, 4);
		s.push(1, 40);
		s.push(2, 300);
		s.push(2, 400);
		s.push(0, 5);
		s.push(1, 50);
		s.push(2, 500);
		assertEquals(4, s.pop(0));
		assertEquals(3, s.pop(0));
		assertEquals(2, s.pop(0));
		assertEquals(1, s.pop(0));
		assertEquals(Integer.MIN_VALUE, s.pop(0));
		assertEquals(40, s.pop(1));
		assertEquals(30, s.pop(1));
		assertEquals(20, s.pop(1));
		assertEquals(10, s.pop(1));
		assertEquals(Integer.MIN_VALUE, s.pop(1));
		assertEquals(400, s.pop(2));
		assertEquals(300, s.pop(2));
		assertEquals(200, s.pop(2));
		assertEquals(100, s.pop(2));
		assertEquals(Integer.MIN_VALUE, s.pop(2));
    }
}
