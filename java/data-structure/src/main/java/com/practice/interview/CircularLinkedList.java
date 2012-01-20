package com.practice.interview;

public class CircularLinkedList
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

	public CircularLinkedList()	{
		head	=	new Node(-1);
		head.setNext(head);
	}

	public Node getLast()	{
		Node	lNode	=	head;
		while ( head != lNode.getNext() )	lNode	=	lNode.getNext();
		return	lNode;
	}

	public void print()	{
		Node	cNode	=	head;
		System.out.print("head");
		while ( head != cNode.getNext() )	{
			cNode	=	cNode.getNext();
			System.out.print(" -> " + cNode.getData());
		}
		System.out.println(" -> head");
	}

	public void add(final int nData)	{
		Node	lNode	=	getLast();
		Node	nNode	=	new Node(nData);
		nNode.setNext(head);
		lNode.setNext(nNode);
	}

	public Node search(final int sData)	{
		Node	cNode	=	head;
		while ( head != cNode.getNext() )	{
			cNode	=	cNode.getNext();
			if ( cNode.getData() == sData )	return	cNode;
		}
		return	null;
	}

	public void delete(final int dData)	{
		Node	pNode	=	head;
		Node	dNode	=	pNode.getNext();
		while ( head != dNode )	{
			if ( dNode.getData() == dData )	break;
			pNode	=	dNode;
			dNode	=	dNode.getNext();
		}
		pNode.setNext(dNode.getNext());
		dNode	=	null;
	}

	public void reverse()	{
		Node	pNode	=	head;
		Node	cNode	=	head.getNext();
		if ( head == cNode )	return;
		Node	cnNode	=	cNode.getNext();
		while ( head != cnNode )	{
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
