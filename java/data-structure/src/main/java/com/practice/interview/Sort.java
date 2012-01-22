package com.practice.interview;

import	org.apache.log4j.Logger;

public class Sort
{
	private static Logger	log	=	Logger.getLogger(Sort.class);

	private static void printArr(final int[] arr)	{
		StringBuffer	sb	=	new StringBuffer();
		for ( final int i : arr )
			sb.append(" " + i);
		log.debug(sb.toString());
	}

	public static int[] insertionSort(final int[] arr)	{
		int	i	=	0;
		int	j	=	0;
		int	x	=	0;
		for ( i = 1; i < arr.length; ++i )	{
			x = arr[i];
			j = i - 1;
			while ( 0 <= j && x < arr[j] )	{
				arr[j + 1] = arr[j];
				--j;
			}
			arr[j + 1] = x;
		}
		return	arr;
	}

	public static int[] selectionSort(final int[] arr)	{
		for ( int i = arr.length - 1; i > 0; --i )	{
			int	maxIdx	=	0;
			for ( int j = 1; j < i; ++j )	{
				if ( arr[maxIdx] < arr[j] )	{
					maxIdx	=	j;
				}
			}
			if ( arr[i] < arr[maxIdx] )	{
				int	tmp	=	arr[maxIdx];
				arr[maxIdx]	=	arr[i];
				arr[i]	=	tmp;
			}
		}
		return	arr;
	}

	public static int[] bubbleSort(final int[] arr)	{
		for ( int i = 0; i < arr.length; ++i )	{
			for ( int j = 0; j < arr.length - 1; ++j )	{
				if ( arr[j + 1] < arr[j] )	{
					int	tmp	=	arr[j];
					arr[j]	=	arr[j + 1];
					arr[j + 1]	=	tmp;
				}
			}
		}
		return	arr;
	}

	/*
	public static int[] quickSort(final int[] arr, final int start, final int end)	{
		if ( start < 0 || arr.length - 1 < end || end < 1 )	return	null;
		int	pivot	=	arr[start];
		int	left	=	start + 1;
		int	right	=	end;
		printArr(arr);
		do	{
			while ( arr[left] < pivot )	++left;
			while ( pivot < arr[right] )	--right;
			log.debug("left[" + left + "] = " + arr[left] + "\tright[" + right + "] = " + arr[right]);
			if ( left < right )	{
				int	tmp	=	arr[left];
				arr[left]	=	arr[right];
				arr[right]	=	tmp;
			}
		}	while ( left <= right );
		log.debug("start[" + start + "] = " + arr[start] + "\tright[" + right + "] = " + arr[right]);
		if ( right != start && arr[right] < pivot )	{
			int	tmp	=	arr[right];
			arr[right]	=	pivot;
			arr[start]	=	tmp;
		}
		quickSort(arr, start, right - 1);
		quickSort(arr, right + 1, end);

		return	arr;
		int	i = 0, j = 0, pivot = 0, temp = 0;
		if ( start < end )	{
			i = start;
			j = end + 1;
			pivot	=	arr[start];
			do	{
				do	{
					++i;
				}	while ( arr[i] < pivot );
				do	{
					++j;
				}	while ( pivot < arr[j] );
				if ( i < j )	{
					temp	=	arr[j];
					arr[j]	=	arr[i];
					arr[i]	=	temp;
				}
			}	while ( i <= j );
			temp	=	arr[j];
			arr[j]	=	arr[start];
			arr[start]	=	temp;
			quickSort(arr, start, j - 1);
			quickSort(arr, j + 1, end);
		}
		return	arr;
	}
	*/
}
