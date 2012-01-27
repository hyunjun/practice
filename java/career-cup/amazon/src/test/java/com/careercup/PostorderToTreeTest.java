package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.List;

public class PostorderToTreeTest
{
	@Test
    public void testPostorderToTree()
	{
		PostorderToTree	ptt	=	new PostorderToTree();
		ptt.create("143675", "134567");
		ptt.traversePreorder();
	}
}
