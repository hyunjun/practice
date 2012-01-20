package com.practice.interview;

public class Stack
{
	private int	top;
	private int[]	data;

	public Stack(final int size)	{
		top	=	-1;
		data	=	new int[size];
	}

	public void push(final int nData)	{
		if ( top < data.length - 1 )
			data[++top]	=	nData;
	}

	public int pop()	{
		if ( -1 < top )
			return	data[top--];
		return	-1;
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
