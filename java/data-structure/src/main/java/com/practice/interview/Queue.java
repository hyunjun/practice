package com.practice.interview;

public class Queue<T>
{
	public class Elem<T>	{
		private T	data;
		private Elem	next;
		public Elem(final T data)	{	this.data	=	data;	}
		public T getData()	{	return	this.data;	}
		public void setNext(final Elem next)	{	this.next	=	next;	}
		public Elem getNext()	{	return	this.next;	}
	}

	private Elem<T>	head;

	public Queue()	{
		head	=	new Elem<T>(null);
		head.setNext(null);
	}

	public void print()	{
		System.out.print("head");
		Elem<T>	cElem	=	head.getNext();
		while ( null != cElem )	{
			System.out.print(" -> " + cElem.getData());
			cElem	=	cElem.getNext();
		}
		System.out.println(" -> null");
	}

	public Elem<T> getLast()	{
		Elem<T>	cElem	=	head;
		while ( null != cElem.getNext() )	{
			cElem	=	cElem.getNext();
		}
		return	cElem;
	}

	public void add(final T nData)	{
		Elem<T>	lElem	=	getLast();
		Elem<T>	nElem	=	new Elem<T>(nData);
		nElem.setNext(lElem.getNext());
		lElem.setNext(nElem);
	}

	public T remove()	{
		Elem<T>	dElem	=	head.getNext();
		if ( null != dElem )	{
			head.setNext(dElem.getNext());
			T	result	=	dElem.getData();
			dElem	=	null;
			return	result;
		}
		return	null;
	}

    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
