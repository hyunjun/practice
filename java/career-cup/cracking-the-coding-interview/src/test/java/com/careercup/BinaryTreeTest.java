package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

public class BinaryTreeTest 
{
	//	4.1
	@Test
    public void testIsBalanced()	{
		BinaryTree	bt	=	new BinaryTree(5);
		assertEquals(true, bt.isBalanced());
		bt.insertLeft(5, 3);
		bt.insertLeft(3, 1);
		assertEquals(false, bt.isBalanced());
		bt.insertRight(5, 7);
		bt.insertRight(7, 9);
		assertEquals(true, bt.isBalanced());
    }

	//	4.3
	@Test
	public void testCreateBTFromArray()	{
		BinaryTree	bt	=	new BinaryTree();
		bt.createBTFromArray(new int[] { 1, 2, 3, 4, 5, 6 });
		bt.traverseInorder();
		assertEquals(3, bt.getDepth());
	}

	//	4.4
	@Test
	public void testCreateLL()	{
		BinaryTree	bt	=	new BinaryTree(5);
		bt.insertLeft(5, 3);
		bt.insertLeft(3, 1);
		bt.insertRight(3, 2);
		bt.insertRight(5, 7);
		bt.insertLeft(7, 6);
		bt.insertRight(7, 9);
		bt.insertLeft(9, 8);
		assertEquals(4, bt.getDepth());
		bt.createLL();
	}

	//	4.5
	@Test
	public void testGetNext()	{
		BinaryTree	bt	=	new BinaryTree(5);
		bt.insertLeft(5, 3);
		bt.insertLeft(3, 1);
		bt.insertRight(3, 2);
		bt.insertRight(5, 7);
		bt.insertLeft(7, 6);
		bt.insertRight(6, 10);
		bt.insertRight(10, 11);
		bt.insertRight(7, 9);
		bt.insertLeft(9, 8);
		bt.traverseInorder();
		assertEquals(3, bt.getNext(1).getData());
		assertEquals(2, bt.getNext(3).getData());
		assertEquals(5, bt.getNext(2).getData());
		assertEquals(6, bt.getNext(5).getData());
		assertEquals(10, bt.getNext(6).getData());
		assertEquals(11, bt.getNext(10).getData());
		assertEquals(7, bt.getNext(11).getData());
		assertEquals(8, bt.getNext(7).getData());
		assertEquals(9, bt.getNext(8).getData());
		assertEquals(null, bt.getNext(9));
	}

	//	4.6
	@Test
	public void testFindCA()	{
		BinaryTree	bt	=	new BinaryTree(5);
		bt.insertLeft(5, 3);
		bt.insertLeft(3, 1);
		bt.insertRight(3, 2);
		bt.insertRight(5, 7);
		bt.insertLeft(7, 6);
		bt.insertRight(6, 10);
		bt.insertRight(10, 11);
		bt.insertRight(7, 9);
		bt.insertLeft(9, 8);
		assertEquals(5, bt.findCA(3, 6));
		assertEquals(3, bt.findCA(1, 2));
		assertEquals(7, bt.findCA(11, 9));
		assertEquals(5, bt.findCA(1, 11));
	}

	//	4.8
	@Test
	public void testFindPath()	{
		BinaryTree	bt	=	new BinaryTree(0);
		bt.insertLeft(0, 1);
		bt.insertRight(0, 2);
		bt.insertLeft(1, 4);
		bt.insertRight(1, 5);
		bt.insertLeft(2, 3);
		bt.insertRight(2, 4);
		bt.findPath(5);
	}
}
