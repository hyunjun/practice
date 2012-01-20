package com.practice.interview;

public class LinkedList
{
	public class Node	{
		private int	data;
		private Node	next;
		public Node(final int data)	{	this.data	=	data;	}
		public int getData()	{	return	this.data;	}
		public void setNext(final Node next)	{	this.next	=	next;	}
		public Node getNext()	{	return	this.next;	}
	}

	private Node	head;

	public LinkedList()	{
		head	=	new Node(-1);
		head.setNext(null);
	}

	public Node getLast()	{
		Node	lNode	=	head;
		while ( null != lNode.getNext() )	lNode	=	lNode.getNext();
		return	lNode;
	}

	public void print()	{
		Node	cNode	=	head;
		System.out.print("head");
		while ( null != cNode.getNext() )	{
			cNode	=	cNode.getNext();
			System.out.print(" -> " + cNode.getData());
		}
		System.out.println(" -> end");
	}

	public void add(final int nData)	{
		Node	lNode	=	getLast();
		Node	nNode	=	new Node(nData);
		lNode.setNext(nNode);
	}

	public Node search(final int sData)	{
		Node	cNode	=	head;
		while ( null != cNode.getNext() )	{
			cNode	=	cNode.getNext();
			if ( cNode.getData() == sData )	return	cNode;
		}
		return	null;
	}

	public void delete(final int dData)	{
		Node	dNode	=	head;
		Node	pNode	=	null;
		while ( null != dNode.getNext() )	{
			pNode	=	dNode;
			dNode	=	dNode.getNext();
			if ( dNode.getData() == dData )	break;
		}
		pNode.setNext(dNode.getNext());
		dNode	=	null;
	}

	public void reverse()	{
		Node	pNode	=	null;
		Node	cNode	=	head.getNext();
		if ( null == cNode )	return;
		Node	cnNode	=	cNode.getNext();
		while ( null != cnNode )	{
			cNode.setNext(pNode);
			pNode	=	cNode;
			cNode	=	cnNode;
			cnNode	=	cNode.getNext();
		}
		cNode.setNext(pNode);
		head.setNext(cNode);
	}

    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
