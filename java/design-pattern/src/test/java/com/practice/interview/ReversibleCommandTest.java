package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class ReversibleCommandTest	{
	@Test
	public void testCommand()	{
		Panel	panel	=	new Panel();
		CommandStack	cs	=	new CommandStack();
		cs.execute(new PanelChangeCommand(panel, "ORANGE"));
		cs.execute(new PanelChangeCommand(panel, "YELLOW"));
		cs.execute(new PanelChangeCommand(panel, "GREEN"));

		System.out.println("undo twice");
		cs.undo();
		cs.undo();
		System.out.println("redo once");
		cs.redo();
		cs.execute(new PanelChangeCommand(panel, "BLUE"));
	}
}

