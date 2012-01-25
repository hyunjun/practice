package com.careercup;

public class Stack	{
	private int	top;
	private int[]	arr;
	public Stack(int size)	{
		top	=	-1;
		arr	=	new int[size];
	}
	public void push(int data)	{
		if ( top < arr.length - 1 )
			arr[++top]	=	data;
	}
	public int pop()	{
		if ( -1 < top )
			return	arr[top--];
		return	Integer.MIN_VALUE;
	}
	public boolean isFull()	{
		return	top == arr.length - 1 ? true : false;
	}
	public boolean isEmpty()	{
		return	top == -1 ? true : false;
	}
	public String toString()	{
		StringBuffer	sb	=	new StringBuffer("top: " + top + "\ndata:");
		if ( false == isEmpty() )
			for ( int i = 0; i <= top;	++i )
				sb.append("\t" + arr[i]);
		return	sb.toString();
	}
}
