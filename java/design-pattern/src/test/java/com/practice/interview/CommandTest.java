package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.ArrayList;
import	java.util.Enumeration;
import	java.util.List;

public class CommandTest	{
	@Test
	public void testCommand()	{
		List<Command>	cmds	=	new ArrayList<Command>();

		cmds.add(new Command()	{
			@Override
			public void execute()	{	System.out.println("work");	}
		});
		cmds.add(new Command()	{
			@Override
			public void execute()	{	System.out.println("eat");	}
		});
		for ( Command cmd : cmds )
			cmd.execute();
	}
}

