package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.ArrayList;
import	java.util.List;

public class MatrixTest	{
	@Test
	public void testGetMatrixNum()	{
		int[][]	arr30	=	new int[][] {
			{ 1, -1, 2 },
			{ -2, 3, -3 },
			{ 4, -4, 5 },
		};
		assertEquals(5, Matrix.getMaxSum(arr30));
		assertEquals(5, Matrix.getMaxMatrix(arr30));
		int[][]	arr31	=	new int[][] {
			{ 1, -1, 2 },
			{ -2, 3, 3 },
			{ 4, -4, 5 },
		};
		assertEquals(11, Matrix.getMaxSum(arr31));
		assertEquals(11, Matrix.getMaxMatrix(arr31));
		int[][]	arr32	=	new int[][] {
			{ -1, 1, 2 },
			{ -2, 3, 3 },
			{ -4, 4, 5 },
		};
		assertEquals(18, Matrix.getMaxSum(arr32));
		assertEquals(18, Matrix.getMaxMatrix(arr32));
	}
}
