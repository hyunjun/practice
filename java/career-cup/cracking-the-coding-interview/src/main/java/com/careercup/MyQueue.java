package com.careercup;

//	3.5 MyQueue class using two stacks
public class MyQueue	{
	private Stack	add;
	private Stack	remove;

	public MyQueue(int size)	{
		add	=	new Stack(size);
		remove	=	new Stack(size);
	}
	public void add(int data)	{
		if ( false == add.isFull() )
			add.push(data);
	}
	public int remove()	{
		int	result	=	Integer.MIN_VALUE;
		if ( false == add.isEmpty() )	{
			while ( false == add.isEmpty() )
				remove.push(add.pop());
			result	=	remove.pop();
			while ( false == remove.isEmpty() )
				add.push(remove.pop());
		}
		return	result;
	}
	public String toString()	{
		StringBuffer	sb	=	new StringBuffer("add\n" + add.toString() + "\nremove\n" + remove.toString());
		return	sb.toString();
	}
}
