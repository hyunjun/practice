package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

//	8.2
public class Robot	{
	public static int getPath(int M, int N)	{
		if ( M == 1 || N == 1 )	return	1;
		return	getPath(M - 1, N) + getPath(M, N - 1);
	}

	public class Node	{
		private int	m, n;
		private Node	left;
		private Node	right;
		private boolean	visited;
		public Node(int m, int n)	{
			this.m	=	m;
			this.n	=	n;
			left	=	null;
			right	=	null;
			visited	=	false;
		}
		public int getM()	{	return	m;	}
		public int getN()	{	return	n;	}
		public void setLeft(Node left)	{	this.left	=	left;	}
		public Node getLeft()	{	return	this.left;	}
		public void setRight(Node right)	{	this.right	=	right;	}
		public Node getRight()	{	return	this.right;	}
		public void setVisited(boolean visited)	{	this.visited	=	visited;	}
		public boolean isVisited()	{	return	this.visited;	}
	}

	private Node	root;

	public void createTree(int M, int N)	{
		root	=	new Node(M, N);
		List<Node>	list	=	new ArrayList<Node>();
		list.add(root);
		while ( list.size() > 0 )	{
			Node	c	=	list.remove(0);
			if ( c.getM() > 1 )	{
				Node	left	=	new Node(c.getM() - 1, c.getN());
				c.setLeft(left);
				list.add(left);
			}
			if ( c.getN() > 1 )	{
				Node	right	=	new Node(c.getM(), c.getN() - 1);
				c.setRight(right);
				list.add(right);
			}
		}
	}

	public void printPath(int M, int N)	{
		List<Node>	list	=	new ArrayList<Node>();
		list.add(root);
		while ( list.size() > 0 )	{
			Node	c	=	list.get(list.size() - 1);
			c.setVisited(true);
			Node	left	=	c.getLeft();
			if ( left != null && left.isVisited() == false )
				list.add(left);
			Node	right	=	c.getRight();
			if ( right != null && right.isVisited() == false )
				list.add(right);
			if ( left == null && right == null )	{
				for ( Node n : list )
					if ( n.isVisited() )
						System.out.print("\t(" + n.getM() + ", " + n.getN() + ")");
				System.out.println();
				list.remove(list.size() - 1);
			}
			if ( ( left != null && left.isVisited() ) ||
				( right != null && right.isVisited() ) )
				list.remove(list.size() - 1);
		}
	}
}

