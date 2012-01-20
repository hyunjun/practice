package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class CircularLinkedListTest
{
	@Test
    public void testCircularLinkedList()
    {
        CircularLinkedList	cll	=	new CircularLinkedList();
        assertNotNull(cll);
		assertEquals(-1, cll.getLast().getData());
		cll.print();
		cll.add(1);
		cll.print();
		assertEquals(1, cll.getLast().getData());
		cll.add(2);
		cll.print();
		assertEquals(2, cll.getLast().getData());
		cll.add(4);
		cll.print();
		assertEquals(4, cll.getLast().getData());
		assertEquals(1, cll.search(1).getData());
		assertEquals(2, cll.search(2).getData());
		assertEquals(4, cll.search(4).getData());
		assertEquals(null, cll.search(5));
		cll.reverse();
		cll.print();
		cll.delete(2);
		cll.print();
		assertEquals(null, cll.search(2));
		cll.delete(1);
		cll.print();
		assertEquals(null, cll.search(1));
		cll.delete(4);
		cll.print();
		assertEquals(null, cll.search(4));
		assertEquals(-1, cll.getLast().getData());
		cll.print();
    }
}
