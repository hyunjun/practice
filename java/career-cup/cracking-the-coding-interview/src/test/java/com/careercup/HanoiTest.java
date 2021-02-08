package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

//	3.4
public class HanoiTest
{
	@Test
    public void testHanoi()
    {
		Hanoi	h	=	new Hanoi(15);
		System.out.println(h);
		h.move();
		System.out.println(h);
    }
}
