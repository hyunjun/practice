package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class QueueTest
{
	@Test
    public void testQueue()
    {
		Queue	q	=	new Queue();
		q.print();
		assertEquals(-1, q.getLast().getData());
		q.add(1);
		q.print();
		assertEquals(1, q.getLast().getData());
		q.add(2);
		q.print();
		assertEquals(2, q.getLast().getData());
		q.add(3);
		q.print();
		assertEquals(3, q.getLast().getData());
		q.add(4);
		q.print();
		assertEquals(4, q.getLast().getData());
		q.add(5);
		q.print();
		assertEquals(5, q.getLast().getData());
		q.remove();
		q.print();
		assertEquals(5, q.getLast().getData());
		q.remove();
		q.print();
		assertEquals(5, q.getLast().getData());
		q.remove();
		q.print();
		assertEquals(5, q.getLast().getData());
		q.remove();
		q.print();
		assertEquals(5, q.getLast().getData());
		q.remove();
		q.print();
		assertEquals(-1, q.getLast().getData());
    }
}
