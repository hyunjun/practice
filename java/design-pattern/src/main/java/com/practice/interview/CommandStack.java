package com.practice.interview;

import	java.util.ArrayList;
import	java.util.List;

//	http://iilii.egloos.com/5378691
public class CommandStack	{
	private int	current	=	-1;
	private List<ReversibleCommand>	commands	=	new ArrayList<ReversibleCommand>();

	public void execute(ReversibleCommand c)	{
		for ( int i = commands.size() - 1; i > current; --i )	{
			commands.remove(i);
		}
		commands.add(c);
		redo();
	}
	public void redo()	{
		commands.get(++current).redo();
	}
	public void undo()	{
		commands.get(current--).undo();
	}
}

