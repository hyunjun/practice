package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class BinarySearchTreeTest
{
	@Test
    public void testBinarySearchTree()
    {
		BinarySearchTree	bt	=	new BinarySearchTree();
		bt.insert(6);
		assertEquals(6, bt.search(6).getData());
		bt.insert(3);
		assertEquals(3, bt.search(3).getData());
		bt.insert(9);
		assertEquals(9, bt.search(9).getData());
		bt.insert(1);
		assertEquals(1, bt.search(1).getData());
		bt.insert(5);
		assertEquals(5, bt.search(5).getData());
		bt.insert(7);
		assertEquals(7, bt.search(7).getData());
		bt.insert(12);
		assertEquals(12, bt.search(12).getData());
		bt.traverseInorder();	//	1 3 5 6 7 9 12
		bt.traversePreorder();	//	6 3 1 5 9 7 12
		bt.traversePostorder();	//	1 5 3 7 12 9 6
		/*
		assertTrue(bt.remove(9));
		bt.traverseInorder();
		bt.traversePreorder();
		bt.traversePostorder();
		*/
    }
}
