package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

//	20.11
public class Square	{
	public static int getSquareNum(int[][] arr)	{
		int	ret	=	0;
		for ( int i = 0; i < arr.length; ++i )
			for ( int j = 0; j < arr[i].length; ++j )	{
				//System.out.println("(" + i + ", " + j + ")\tmax = " + (arr[i].length - Math.max(i, j)));
				ret	+=	getSquareNum(arr, i, j, arr[i].length - Math.max(i, j));
			}
		return	ret;
	}
	private static int getSquareNum(int[][] arr, int x, int y, int max)	{
		int	ret	=	0;
		for ( int size = max; size > 0; --size )	{
			//System.out.print("\tstart(" + x + ", " + y + ")\tsize = " + size);
			boolean	isSquare	=	true;
			for ( int i = x; i < x + size; ++i )	{
				for ( int j = y; j < y + size; ++j )	{
					//System.out.print("\tarr[" + i + "][" + j + "] = " + arr[i][j]);
					if ( arr[i][j] != 1 )	{
						isSquare	=	false;
						break;
					}
				}
				if ( false == isSquare )
					break;
			}
			if ( isSquare )	{
				//System.out.print("\tsquare");
				++ret;
			}
			//System.out.println();
		}
		return	ret;
	}
}

