package com.practice.interview;

//	Generic Stack
//	See Effective Java, 2nd edition, Item 26
public class Stack<T>
{
	private int	top;
	private T[]	data;

	public Stack(final int size)	{
		top	=	-1;
		data	=	(T[]) new Object[size];
	}

	public void push(final T nData)	{
		if ( top < data.length - 1 )
			data[++top]	=	nData;
	}

	public T pop()	{
		if ( -1 < top )	{
			T	result	=	data[top];
			data[top]	=	null;
			--top;
			return	result;
		}
		return	null;
	}

	public boolean isEmpty()	{
		if ( -1 == top )
			return	true;
		return	false;
	}

	public void print()	{
		System.out.print("-1");
		if ( -1 < top )
			for ( int i = 0; i <= top; ++i )	{
				System.out.print(" -> " + data[i]);
			}
		System.out.println("\ttop: " + top);
	}

    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
