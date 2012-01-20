package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

public class SumOfThreeNumbersTest
{
	@Test
    public void testSumOfThreeNumbers()
	{
		SumOfThreeNumbers	c	=	new SumOfThreeNumbers();
		assertArrayEquals(new int[] { -1, 0, 1 },
				c.getArrays(new int[] { -1, 0, 1, 2 }));
		assertArrayEquals(new int[] { -4, -1, 5 },
				c.getArrays(new int[] { -4, -1, 0, 2, 5, 7 }));
	}
}
