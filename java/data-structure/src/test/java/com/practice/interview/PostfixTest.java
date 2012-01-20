package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class PostfixTest
{
	private static Postfix	postfix;

	@BeforeClass
	public static void setUp()	{
		postfix	=	new Postfix();
	}
	@AfterClass
	public static void tearDown()	{
	}

	@Test
    public void testGetTokens()
    {
		assertArrayEquals(
			new String[] { "28", "/", "4", "+", "3", "*", "2" },
			postfix.getTokens("28/4+3*2"));
		assertArrayEquals(
			new String[] { "28", "/", "(", "4", "+", "3", ")", "*", "2" },
			postfix.getTokens("28/(4+3)*2"));
		assertArrayEquals(
			new String[] { "28", "/", "(", "(", "4", "+", "3", ")", "*", "2", ")" },
			postfix.getTokens("28/((4+3)*2)"));
		assertArrayEquals(
			new String[] { "(", "28", "/", "(", "(", "4", "+", "3", ")", "*", "2", ")", ")" },
			postfix.getTokens("(28/((4+3)*2))"));
    }

	@Test
	public void testConvert()	{
		postfix.convert("28/4+3*2");
		assertEquals(13, postfix.calc());
		postfix.convert("28/(4+3)*2");
		assertEquals(8, postfix.calc());
		postfix.convert("28/((4+3)*2)");
		assertEquals(2, postfix.calc());
		postfix.convert("(28/((4+3)*2))");
		assertEquals(2, postfix.calc());
	}
}
