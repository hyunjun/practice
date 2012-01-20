package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class DoublyLinkedListTest
{
	@Test
    public void testDoublyLinkedList()
    {
        DoublyLinkedList	dll	=	new DoublyLinkedList();
        assertNotNull(dll);
		assertEquals(-1, dll.getLast().getData());
		dll.print();
		dll.insertAfter(1, 1);
		dll.print();
		assertEquals(1, dll.search(1).getData());
		dll.insertAfter(1, 2);
		dll.print();
		assertEquals(2, dll.search(2).getData());
		dll.insertAfter(2, 4);
		dll.print();
		assertEquals(4, dll.search(4).getData());
		dll.insertBefore(4, 3);
		dll.print();
		assertEquals(3, dll.search(3).getData());
		dll.insertBefore(1, 0);
		dll.print();
		assertEquals(0, dll.search(0).getData());
		dll.reverse();
		dll.print();
		assertEquals(3, dll.search(4).getNext().getData());
		assertEquals(2, dll.search(3).getNext().getData());
		assertEquals(1, dll.search(2).getNext().getData());
		assertEquals(0, dll.search(1).getNext().getData());
		assertEquals(4, dll.search(3).getPrev().getData());
		assertEquals(3, dll.search(2).getPrev().getData());
		assertEquals(2, dll.search(1).getPrev().getData());
		assertEquals(1, dll.search(0).getPrev().getData());
		dll.delete(2);
		dll.print();
		assertEquals(null, dll.search(2));
		dll.delete(0);
		dll.print();
		assertEquals(null, dll.search(0));
		dll.delete(4);
		dll.print();
		assertEquals(null, dll.search(4));
    }
}
