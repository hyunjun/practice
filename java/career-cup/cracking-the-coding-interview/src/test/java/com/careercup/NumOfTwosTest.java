package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

public class NumOfTwosTest	{
	@Test
	public void testNumOfTwos()	{
		assertEquals(0, NumOfTwos.getNumOfTwo(0));
		assertEquals(0, NumOfTwos.getNumOfTwo(1));
		assertEquals(1, NumOfTwos.getNumOfTwo(2));
		assertEquals(138, NumOfTwos.getNumOfTwo(279));
		assertEquals(202, NumOfTwos.getNumOfTwo(513));

		assertEquals(0, NumOfTwos.count2sR(0));
		assertEquals(0, NumOfTwos.count2sR(1));
		assertEquals(1, NumOfTwos.count2sR(2));
		assertEquals(138, NumOfTwos.count2sR(279));
		assertEquals(202, NumOfTwos.count2sR(513));

		assertEquals(0, NumOfTwos.count2sI(0));
		assertEquals(0, NumOfTwos.count2sI(1));
		assertEquals(1, NumOfTwos.count2sI(2));
		assertEquals(138, NumOfTwos.count2sI(279));
		assertEquals(202, NumOfTwos.count2sI(513));
	}
}
