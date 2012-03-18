package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.List;

public class ReplacePercent20Test
{
	@Test
    public void testReplacePercent20()
	{
		final String	s	=	"http://o=example%20corporation";
		final String	r	=	"http://o=example corporation";
		assertEquals(r, ReplacePercent20.replace(s));
	}
}
