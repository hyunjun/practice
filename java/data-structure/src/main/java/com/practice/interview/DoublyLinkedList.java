package com.practice.interview;

public class DoublyLinkedList
{
	public class DNode	{
		private int	data;
		private DNode	prev;
		private DNode	next;
		public DNode(final int data)	{	this.data	=	data;	}
		public int getData()	{	return	this.data;	}
		public void setPrev(final DNode prev)	{	this.prev	=	prev;	}
		public DNode getPrev()	{	return	this.prev;	}
		public void setNext(final DNode next)	{	this.next	=	next;	}
		public DNode getNext()	{	return	this.next;	}
	}

	private DNode	head;

	public DoublyLinkedList()	{
		head	=	new DNode(-1);
		head.setPrev(head);
		head.setNext(null);
	}

	public DNode getLast()	{
		DNode	lNode	=	head;
		while ( null != lNode.getNext() )	lNode	=	lNode.getNext();
		return	lNode;
	}

	public void print()	{
		DNode	cNode	=	head;
		System.out.print("head");
		while ( null != cNode.getNext() )	{
			cNode	=	cNode.getNext();
			System.out.print(" <-> " + cNode.getData());
		}
		System.out.println(" <-> end");
	}

	public DNode search(final int sData)	{
		DNode	cNode	=	head.getNext();
		while ( null != cNode )	{
			if ( cNode.getData() == sData )	return	cNode;
			cNode	=	cNode.getNext();
		}
		return	null;
	}

	public void insertBefore(final int pData, final int nData)	{
		DNode	pNode	=	search(pData);
		DNode	nNode	=	new DNode(nData);
		if ( null != pNode )	{
			nNode.setPrev(pNode.getPrev());
			nNode.setNext(pNode);
			nNode.getPrev().setNext(nNode);
			pNode.setPrev(nNode);
		}	else	{
			nNode.setPrev(head);
			nNode.setNext(head.getNext());
			head.setNext(nNode);
		}
	}

	public void insertAfter(final int pData, final int nData)	{
		DNode	pNode	=	search(pData);
		DNode	nNode	=	new DNode(nData);
		if ( null != pNode )	{
			nNode.setPrev(pNode);
			nNode.setNext(pNode.getNext());
			if ( null != nNode.getNext() )
				nNode.getNext().setPrev(nNode);
			pNode.setNext(nNode);
		}	else	{
			nNode.setPrev(head);
			nNode.setNext(head.getNext());
			head.setNext(nNode);
		}
	}

	public void delete(final int dData)	{
		DNode	dNode	=	search(dData);
		dNode.getPrev().setNext(dNode.getNext());
		if ( null != dNode.getNext() )
			dNode.getNext().setPrev(dNode.getPrev());
		dNode	=	null;
	}

	public void reverse()	{
		DNode	pNode	=	null;
		DNode	cNode	=	head.getNext();
		if ( null == cNode )	return;
		DNode	cnNode	=	cNode.getNext();
		while ( null != cnNode )	{
			cNode.setNext(pNode);
			cNode.setPrev(cnNode);
			pNode	=	cNode;
			cNode	=	cnNode;
			cnNode	=	cNode.getNext();
		}
		cNode.setNext(pNode);
		cNode.setPrev(head);
		head.setNext(cNode);
	}

    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
