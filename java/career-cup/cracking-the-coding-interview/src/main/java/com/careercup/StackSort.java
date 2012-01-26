package com.careercup;

//	3.6 sort stack using only push, pop, peek, isEmpty
public class StackSort	{
	private Stack[]	stack;
	private int	src;
	private int	tmp;
	private int	dst;

	public StackSort(int size)	{
		stack	=	new Stack[3];
		for ( int i = 0; i < stack.length; ++i )
			stack[i]	=	new Stack(size);
		src	=	0;
		tmp	=	1;
		dst	=	2;
	}
	public void push(int data)	{
		if ( false == stack[src].isFull() )
			stack[src].push(data);
	}
	public void sort()	{
		while ( false == ( stack[src].isEmpty() && stack[tmp].isEmpty() ) )	{
			System.out.println("before moving\n" + this);
			int	min	=	Integer.MAX_VALUE;
			while ( false == stack[src].isEmpty() )	{
				int	data	=	stack[src].pop();
				if ( data < min )	{
					if ( min != Integer.MAX_VALUE )
						stack[tmp].push(min);
					min	=	data;
				}	else
					stack[tmp].push(data);
				System.out.println("min: " + min);
			}
			stack[dst].push(min);
			System.out.println("after moving\n" + this);
			int	t	=	src;
			src	=	tmp;
			tmp	=	t;
		}
	}
	public String toString()	{
		StringBuffer	sb	=	new StringBuffer();
		for ( Stack s : stack )
			sb.append("\n" + s.toString());
		return	sb.toString();
	}
}
