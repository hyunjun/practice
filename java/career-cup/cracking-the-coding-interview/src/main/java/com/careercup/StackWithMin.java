package com.careercup;

//	3.2	stack with push, pop, min in O(1)
public class StackWithMin	{
	private int	top;
	private int[]	dataArr;
	private int[]	minArr;
	public StackWithMin(int size)	{
		top	=	-1;
		dataArr	=	new int[size];
		minArr	=	new int[size];
	}
	public void push(int data)	{
		if ( top < dataArr.length  - 1)	{
			++top;
			dataArr[top]	=	data;
			if ( 0 == top )
				minArr[top]	=	top;
			else	{
				if ( data < dataArr[minArr[top - 1]] )
					minArr[top]	=	top;
				else
					minArr[top]	=	minArr[top - 1];
			}
		}
	}
	public int pop()	{
		if ( -1 < top )
			return	dataArr[top--];
		return	Integer.MIN_VALUE;
	}
	public int min()	{
		if ( -1 < top )
			return	dataArr[minArr[top]];
		return	Integer.MIN_VALUE;
	}
	public String toString()	{
		StringBuffer	sb	=	new StringBuffer("top: " + top + "\ndata:");
		for ( int i = 0; i <= top;	++i )
			sb.append("\t" + dataArr[i]);
		sb.append("\nmin:");
		for ( int i = 0; i <= top;	++i )
			sb.append("\t" + minArr[i]);
		return	sb.toString();
	}
}
