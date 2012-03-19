package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

/**
 *	http://www.careercup.com/question?id=13055672
 */
public class ArrayProduct 
{
	private static Logger	log	=	Logger.getLogger(ArrayProduct.class);

	//	using divide
	public static int[] getArrayProduct0(final int[] arr)	{
		int	product	=	1;
		for ( int i : arr )	product *= i;
		int[]	retArr	=	new int[arr.length];
		for ( int i = 0; i < retArr.length; ++i )
			retArr[i]	=	product / arr[i];
		return	retArr;
	}

	//	not using divide, brutal force
	public static int[] getArrayProduct1(final int[] arr)	{
		int[]	retArr	=	new int[arr.length];
		for ( int i = 0; i < retArr.length; ++i )
			retArr[i]	=	1;

		for ( int i = 0; i < arr.length; ++i )
			for ( int j = 0; j < arr.length; ++j )
				if ( i != j )
					retArr[i] *= arr[j];

		return	retArr;
	}

	//	not using divide, O(n)
	public static int[] getArrayProduct2(final int[] arr)	{
		//	arrA:	product from [0..i]
		int[]	arrA	=	new int[arr.length];
		arrA[0]	=	arr[0];
		for ( int i = 1; i < arr.length; ++i )
			arrA[i]	=	arrA[i - 1] * arr[i];
		//	arrB:	product from [i..arr.length - 1]
		int[]	arrB	=	new int[arr.length];
		arrB[arr.length - 1]	=	arr[arr.length - 1];
		for ( int i = arr.length - 2; i >= 0; --i )
			arrB[i]	=	arrB[i + 1] * arr[i];
		//	retArr[i]	=	arrA[i - 1] * arrB[i + 1];
		int[]	retArr	=	new int[arr.length];
		int	left = 1, right = 1;
		for ( int i = 0; i < arr.length; ++i )	{
			left	=	0 < i ? arrA[i - 1] : 1;
			right	=	i < arr.length - 1 ? arrB[i + 1] : 1;
			retArr[i]	=	left * right;
			log.debug(String.format("[%d]\t%d * %d = %d", i, left, right, retArr[i]));
		}
		return	retArr;
	}
}
