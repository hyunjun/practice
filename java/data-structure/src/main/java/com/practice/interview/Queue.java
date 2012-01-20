package com.practice.interview;

public class Queue
{
	public class Elem	{
		private int	data;
		private Elem	next;
		public Elem(final int data)	{	this.data	=	data;	}
		public int getData()	{	return	this.data;	}
		public void setNext(final Elem next)	{	this.next	=	next;	}
		public Elem getNext()	{	return	this.next;	}
	}

	private Elem	head;

	public Queue()	{
		head	=	new Elem(-1);
		head.setNext(null);
	}

	public void print()	{
		System.out.print("head");
		Elem	cElem	=	head.getNext();
		while ( null != cElem )	{
			System.out.print(" -> " + cElem.getData());
			cElem	=	cElem.getNext();
		}
		System.out.println(" -> null");
	}

	public Elem getLast()	{
		Elem	cElem	=	head;
		while ( null != cElem.getNext() )	{
			cElem	=	cElem.getNext();
		}
		return	cElem;
	}

	public void add(final int nData)	{
		Elem	lElem	=	getLast();
		Elem	nElem	=	new Elem(nData);
		nElem.setNext(lElem.getNext());
		lElem.setNext(nElem);
	}

	public void remove()	{
		Elem	dElem	=	head.getNext();
		head.setNext(dElem.getNext());
		dElem	=	null;
	}

    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
