package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.ArrayList;
import	java.util.List;

public class SquareTest	{
	@Test
	public void testGetSquareNum()	{
		int[][]	arr20	=	new int[][] { { 1, 1 }, { 1, 1 } };
		assertEquals(5, Square.getSquareNum(arr20));
		int[][]	arr21	=	new int[][] { { 0, 1 }, { 1, 1 } };
		assertEquals(3, Square.getSquareNum(arr21));
		int[][]	arr22	=	new int[][] { { 0, 1 }, { 1, 0 } };
		assertEquals(2, Square.getSquareNum(arr22));
		int[][]	arr30	=	new int[][] {
			{ 1, 1, 1 },
			{ 1, 1, 1 },
			{ 1, 1, 1 },
		};
		assertEquals(14, Square.getSquareNum(arr30));
		int[][]	arr40	=	new int[][] {
			{ 0, 1, 0, 1 },
			{ 1, 1, 1, 0 },
			{ 1, 1, 1, 1 },
			{ 1, 1, 1, 0 }
		};
		assertEquals(17, Square.getSquareNum(arr40));
		int[][]	arr41	=	new int[][] {
			{ 0, 1, 1, 1 },
			{ 1, 1, 1, 1 },
			{ 1, 1, 1, 1 },
			{ 1, 1, 1, 0 }
		};
		assertEquals(23, Square.getSquareNum(arr41));
	}
}
