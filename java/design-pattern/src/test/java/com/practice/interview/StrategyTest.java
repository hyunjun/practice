package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.ArrayList;
import	java.util.Enumeration;
import	java.util.List;

public class StrategyTest	{
	@Test
	public void testMart()	{
		Seller	cupSeller	=	new CupSeller();
		Seller	phoneSeller	=	new PhoneSeller();
		Mart	mart1	=	new Mart(cupSeller);
		mart1.order();
		Mart	mart2	=	new Mart(phoneSeller);
		mart2.order();
	}
}

