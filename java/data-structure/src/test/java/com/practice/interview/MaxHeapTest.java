package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class MaxHeapTest
{
	@Test
    public void testMaxHeap()
    {
		MaxHeap	mh	=	new MaxHeap(10);
		mh.add(5);
		mh.print();
		assertEquals(5, mh.peek());
		mh.add(4);
		mh.print();
		assertEquals(5, mh.peek());
		mh.add(1);
		mh.print();
		assertEquals(5, mh.peek());
		mh.add(2);
		mh.print();
		assertEquals(5, mh.peek());
		mh.add(9);
		mh.print();
		assertEquals(9, mh.peek());
		mh.add(3);
		mh.print();
		assertEquals(9, mh.peek());
		mh.add(6);
		mh.print();
		assertEquals(9, mh.peek());
		assertEquals(9, mh.poll());
		assertEquals(6, mh.peek());
		mh.print();
    }
}
