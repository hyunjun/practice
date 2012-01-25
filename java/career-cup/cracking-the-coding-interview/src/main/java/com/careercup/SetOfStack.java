package com.careercup;

//	3.3	Set of stacks
public class SetOfStack	{
	private Stack[]	stack;

	public SetOfStack(int num, int size)	{
		stack	=	new Stack[num];
		//for ( Stack s : stack )	{	//	why error?
		//	s	=	new Stack(size);
		for ( int i = 0; i < stack.length; ++i )	{
			stack[i]	=	new Stack(size);
		}
	}
	public void push(int data)	{
		for ( Stack s : stack )
			if ( false == s.isFull() )	{
				s.push(data);
				break;
			}
	}
	public int pop()	{
		for ( int i = stack.length - 1; i >= 0; --i )	{
			if ( false == stack[i].isEmpty() )
				return	stack[i].pop();
		}
		return	Integer.MIN_VALUE;
	}
	public int popAt(int num)	{
		if ( -1 < num && num < stack.length )
			return	stack[num].pop();
		return	Integer.MIN_VALUE;
	}
	public String toString()	{
		StringBuffer	sb	=	new StringBuffer("num of stack: " + stack.length);
		for ( Stack s : stack )
			sb.append("\n" + s.toString());
		return	sb.toString();
	}
}
