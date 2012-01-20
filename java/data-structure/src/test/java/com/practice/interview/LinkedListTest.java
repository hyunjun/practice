package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class LinkedListTest
{
	@Test
    public void testLinkedList()
    {
        LinkedList	ll	=	new LinkedList();
        assertNotNull(ll);
		assertEquals(-1, ll.getLast().getData());
		ll.print();
		ll.add(1);
		ll.print();
		assertEquals(1, ll.getLast().getData());
		ll.add(2);
		ll.print();
		assertEquals(2, ll.getLast().getData());
		ll.add(4);
		ll.print();
		assertEquals(4, ll.getLast().getData());
		assertEquals(1, ll.search(1).getData());
		assertEquals(2, ll.search(2).getData());
		assertEquals(4, ll.search(4).getData());
		assertEquals(null, ll.search(5));
		ll.reverse();
		ll.print();
		ll.delete(2);
		ll.print();
		assertEquals(null, ll.search(2));
		ll.delete(1);
		ll.print();
		assertEquals(null, ll.search(1));
		ll.delete(4);
		ll.print();
		assertEquals(null, ll.search(4));
		assertEquals(-1, ll.getLast().getData());
		ll.print();
    }
}
