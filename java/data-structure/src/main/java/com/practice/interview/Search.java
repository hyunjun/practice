package com.practice.interview;

import	org.apache.log4j.Logger;

public class Search
{
	private static Logger	log	=	Logger.getLogger(Search.class);

	private static void printArr(final int[] arr)	{
		StringBuffer	sb	=	new StringBuffer();
		for ( final int i : arr )
			sb.append(" " + i);
		log.debug(sb.toString());
	}

	public static boolean binarySearch(final int[] arr, final int target)	{
		int	start	=	0;
		int	end	=	arr.length - 1;
		while ( start <= end )	{
			int	mid	=	(start + end + 1) / 2;
			if ( arr[mid] == target )	return	true;
			else if ( arr[mid] < target )	start	=	mid + 1;
			else if ( target < arr[mid] )	end	=	mid - 1;
		}
		return	false;
	}
}
