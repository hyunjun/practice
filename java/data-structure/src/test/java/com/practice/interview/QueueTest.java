package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class QueueTest
{
	@Test
    public void testQueue()
    {
		Queue<Integer>	q	=	new Queue<Integer>();
		q.print();
		assertEquals(null, q.getLast().getData());
		q.add(1);
		q.print();
		assertEquals(Integer.valueOf(1), q.getLast().getData());
		q.add(2);
		q.print();
		assertEquals(Integer.valueOf(2), q.getLast().getData());
		q.add(3);
		q.print();
		assertEquals(Integer.valueOf(3), q.getLast().getData());
		q.add(4);
		q.print();
		assertEquals(Integer.valueOf(4), q.getLast().getData());
		q.add(5);
		q.print();
		assertEquals(Integer.valueOf(5), q.getLast().getData());
		q.remove();
		q.print();
		assertEquals(Integer.valueOf(5), q.getLast().getData());
		q.remove();
		q.print();
		assertEquals(Integer.valueOf(5), q.getLast().getData());
		q.remove();
		q.print();
		assertEquals(Integer.valueOf(5), q.getLast().getData());
		q.remove();
		q.print();
		assertEquals(Integer.valueOf(5), q.getLast().getData());
		q.remove();
		q.print();
		assertEquals(null, q.getLast().getData());
    }
}
