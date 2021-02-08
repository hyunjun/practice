package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

//	3.5
public class MyQueueTest
{
	@Test
    public void testMyQueue()
    {
		MyQueue	q	=	new MyQueue(5);
		q.add(0);
		q.add(1);
		q.add(2);
		q.add(3);
		q.add(4);
		assertEquals(0, q.remove());
		assertEquals(1, q.remove());
		assertEquals(2, q.remove());
		assertEquals(3, q.remove());
		assertEquals(4, q.remove());
    }
}
