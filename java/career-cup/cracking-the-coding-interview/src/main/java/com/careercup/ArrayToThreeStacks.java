package com.careercup;

//	3.1	a single array into 3 stacks
public class ArrayToThreeStacks	{

	private class InnerStack	{
		private int	top;
		private int stackNum;
		public InnerStack(int stackNum)	{
			this.top	=	-1;
			this.stackNum	=	stackNum;
		}
		public void push(int data)	{
			//if ( 3 * (top + 1) + stackNum < getSize() )
			if ( 3 * (top + 1) + stackNum < arr.length )
				arr[3 * ++top + stackNum]	=	data;
		}
		public int pop()	{
			if ( -1 < top )
				return	arr[3 * top-- + stackNum];
			return	Integer.MIN_VALUE;
		}
		public String toString()	{
			StringBuffer	sb	=	new StringBuffer("stack " + stackNum);
			for ( int i = 0; i <= top; ++i )
				sb.append("\t" + arr[3 * i + stackNum]);
			return	sb.toString();
		}
	}

	private int[]	arr;
	private InnerStack[]	stack;

	public ArrayToThreeStacks(int size)	{
		arr	=	new int[size];
		stack	=	new InnerStack[3];
		for ( int i = 0; i < stack.length; ++i )
			stack[i]	=	new InnerStack(i);
	}

	//public int getSize()	{	return	arr.length;	}
	public void push(int stackNum, int data)	{
		if ( -1 < stackNum && stackNum < stack.length )
			stack[stackNum].push(data);
	}
	public int pop(int stackNum)	{
		if ( -1 < stackNum && stackNum < stack.length )
			return	stack[stackNum].pop();
		return	Integer.MIN_VALUE;
	}
	public String toString()	{
		StringBuffer	sb	=	new StringBuffer("arr: ");
		for ( int i : arr )	sb.append("\t" + i);
		sb.append("\n");
		for ( InnerStack s : stack )
			sb.append(s.toString() + "\n");
		return	sb.toString();
	}
}
