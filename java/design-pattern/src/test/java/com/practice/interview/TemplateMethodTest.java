package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.ArrayList;
import	java.util.Enumeration;
import	java.util.List;

public class TemplateMethodTest	{
	@Test
	public void testWorker()	{
		Worker	designer	=	new Designer();
		designer.work();
		Worker	gamer	=	new Gamer();
		gamer.work();
	}
}
