package com.careercup;

//	3.4 Hanoi
public class Hanoi	{
	private Stack[]	stack;
	private int	N;

	public Hanoi(int N)	{
		this.N	=	N;
		stack	=	new Stack[3];
		//for ( Stack s : stack )	{	//	why error?
		//	s	=	new Stack(size);
		for ( int i = 0; i < stack.length; ++i )
			stack[i]	=	new Stack(N);
		for ( int i = N; i > 0; --i )
			stack[0].push(i);
	}
	public void move()	{
		move(N, 0, 1, 2);
	}
	private void move(int num, int src, int tmp, int dst)	{
		if ( 2 == num )
			stack[tmp].push(stack[src].pop());
		else
			move(num - 1, src, dst, tmp);
		stack[dst].push(stack[src].pop());
		if ( 2 == num )
			stack[dst].push(stack[tmp].pop());
		else
			move(num - 1, tmp, src, dst);
	}
	public String toString()	{
		StringBuffer	sb	=	new StringBuffer("num of disk: " + N);
		for ( Stack s : stack )
			sb.append("\n" + s.toString());
		return	sb.toString();
	}
}
