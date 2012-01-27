package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.List;

public class PreorderToTreeTest
{
	@Test
    public void testPreorderToTree()
	{
		PreorderToTree	ptt	=	new PreorderToTree();
		ptt.create("NNLLL");
		//ptt.create("NLNLL");
		ptt.traversePreorder();
	}
}
