package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class SortTest
{
	private static int[][]	arr	=	{
		new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 },
		new int[] { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 },
		new int[] { 2, 4, 8, 12, 24, 5 },
		new int[] { 21, 32, 43, 12, 8, 28 },
		new int[] { 21, 19, 30, 28, 10, 12, 6, 24 },
	};

	private static int[][]	expected	=	{
		new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 },
		new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 },
		new int[] { 2, 4, 5, 8, 12, 24 },
		new int[] { 8, 12, 21, 28, 32, 43},
		new int[] { 6, 10, 12, 19, 21, 24, 28, 30 },
	};

	@Test
    public void testInsertionSort()	{
		for ( int i = 0; i < arr.length; ++i )
			assertArrayEquals(expected[i], Sort.insertionSort(arr[i]));
    }

	@Test
    public void testSelectionSort()	{
		for ( int i = 0; i < arr.length; ++i )
			assertArrayEquals(expected[i], Sort.selectionSort(arr[i]));
    }

	@Test
    public void testBubbleSort()	{
		for ( int i = 0; i < arr.length; ++i )
			assertArrayEquals(expected[i], Sort.bubbleSort(arr[i]));
    }

	/*
	@Test
    public void testQuickSort()	{
		for ( int i = 0; i < arr.length; ++i )
			assertArrayEquals(expected[i], Sort.quickSort(arr[i], 0, arr.length));
    }
	*/
}
