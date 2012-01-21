package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class BinaryTreeTest
{
	@Test
    public void testBinaryTree()
    {
		BinaryTree<Integer>	bt	=	new BinaryTree<Integer>(6);
		assertNotNull(bt.search(6));
		assertTrue(bt.insertLeft(6, 3));
		assertEquals(Integer.valueOf(3), bt.search(6).getLeft().getData());
		assertTrue(bt.insertRight(6, 9));
		assertEquals(Integer.valueOf(9), bt.search(6).getRight().getData());
		assertFalse(bt.insert(6, true, 4));
		assertNull(bt.search(4));
		assertFalse(bt.insert(6, false, 8));
		assertNull(bt.search(8));
		assertTrue(bt.insertLeft(3, 1));
		assertEquals(Integer.valueOf(1), bt.search(3).getLeft().getData());
		assertTrue(bt.insertRight(3, 5));
		assertEquals(Integer.valueOf(5), bt.search(3).getRight().getData());
		assertTrue(bt.insertLeft(9, 7));
		assertEquals(Integer.valueOf(7), bt.search(9).getLeft().getData());
		assertTrue(bt.insertRight(9, 12));
		assertEquals(Integer.valueOf(12), bt.search(9).getRight().getData());
		bt.traverseInorder();
		bt.traversePreorder();
		bt.traversePostorder();
		assertTrue(bt.delete(9));
		bt.traverseInorder();
		bt.traversePreorder();
		bt.traversePostorder();
    }
}
