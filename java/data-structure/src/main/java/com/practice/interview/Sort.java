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

	public static int[] quickSort(final int[] arr)	{
		quickSort(arr, 0, arr.length - 1);
		return	arr;
	}

	public static int[] quickSort(final int[] arr, final int start, final int end)	{
		if ( null == arr || 0 == arr.length || 1 == arr.length )	return	arr;
		int	pivot	=	start;
		int	left	=	start + 1;
		int	right	=	end;
		while ( left < right )	{
			while ( left < right && arr[pivot] < arr[right] )	--right;
			while ( left < right && arr[pivot] > arr[left] )	++left;
			if ( left != right && arr[left] > arr[right] )	{
				int	tmp	=	arr[left];
				arr[left]	=	arr[right];
				arr[right]	=	tmp;
			}
		}
		if ( arr[pivot] > arr[left] )	{
			int	tmp	=	arr[left];
			arr[left]	=	arr[pivot];
			arr[pivot]	=	tmp;
			pivot	=	left;
		}
		if ( start < pivot - 1 )	quickSort(arr, start, pivot - 1);
		if ( pivot + 1 < end )		quickSort(arr, pivot + 1, end);

		return	arr;
	}

	//	http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/Database/algorithm/Quick_Sort
	/*
	public static int[] quickSort(final int[] arr, final int start, final int end)	{
		int	left	=	start;
		int	right	=	end;
		int pivot = arr[left]; // 0번째 원소를 피봇으로 선택
		log.debug("start: pivot = " + pivot + "\tstart = " + left + "\tend = " + right);
		printArr(arr);
		while (left < right)
		{
			// 값이 선택한 피봇과 같거나 크다면, 이동할 필요가 없다
			while ((arr[right] >= pivot) && (left < right))	{
				right --;
				log.debug("\tright: = " + right);
			}
			// 그렇지 않고 값이 피봇보다 작다면,
			// 피봇의 위치에 현재 값을 넣는다.
			if (left != right) {
				arr[left] = arr[right];
			}
			// 왼쪽부터 현재 위치까지 값을 읽어들이면서
			// 피봇보다 큰 값이 있다면, 값을 이동한다.
			while ((arr[left] <= pivot) && (left < right)) 	{
				left ++;
				log.debug("\tleft: = " + left);
			}
			if (left != right) {
				arr[right] = arr[left];
				right --;
			}
		}
		// 모든 스캔이 끝났다면, 피봇값을 현재 위치에 입력한다.
		// 이제 피봇을 기준으로 왼쪽에는 피봇보다 작거나 같은 값만 남았다.
		arr[left] = pivot;
		pivot = left;
		left = start;
		right = end;

		// 재귀호출을 수행한다.
		if (left < pivot)	{
			log.debug("\trecursive call when left " + left + " < pivot " + pivot + ": start = " + left + "\tend = " + (pivot - 1));
			quickSort(arr, left, pivot - 1);
		}
		if (right > pivot) 	{
			log.debug("\trecursive call when pivot " + pivot + " < right " + right + ": start = " + (pivot + 1) + "\tend = " + right);
			quickSort(arr, pivot+1, right);
		}
		return	arr;
	}
	*/
}
