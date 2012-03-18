package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.List;

public class BiggestConsecutiveTest
{
	@Test
    public void testBiggestConsecutive()
	{
		assertEquals(null, BiggestConsecutive.getConsecutive(null));
		assertEquals(null, BiggestConsecutive.getConsecutive(""));
		assertEquals("bca", BiggestConsecutive.getConsecutive("bca"));
		assertEquals("acb", BiggestConsecutive.getConsecutive("acb"));
		assertEquals("bcad", BiggestConsecutive.getConsecutive("bcad"));
		assertEquals("acefgdbdfdfdffd", BiggestConsecutive.getConsecutive("hllsacefgdbdfdfdffd"));
	}
}
