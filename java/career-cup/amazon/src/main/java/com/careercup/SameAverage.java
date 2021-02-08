package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

/**
 *	http://www.careercup.com/question?id=12347514
 */
public class SameAverage
{
	private Logger	log	=	Logger.getLogger(this.getClass());

	public SameAverage(){}

	public List<List<Integer>> getListOfIdxList(final int n, final int r)	{
		List<List<Integer>>	listOfIdxList	=	new ArrayList<List<Integer>>();

		if ( r == 1 )	{
			for ( int i = 0; i < n; ++i )	{
				List<Integer>	list	=	new ArrayList<Integer>();
				list.add(i);
				listOfIdxList.add(list);
			}
			return	listOfIdxList;
		}

		int	i	=	0;
		int[]	nums	=	new int[r];
		nums[0]	=	0;
		while ( 0 <= i )	{
			if ( 0 == i )	{
				if ( nums[i] <= n - r + i )	{
					++i;
					nums[i] = nums[i - 1] + 1;
				}	else	{
					--i;
				}
			}	else if ( r - 1 == i )	{
				//	add list
				List<Integer>	list	=	new ArrayList<Integer>(r);
				for ( int j = 0; j < r; ++j )	list.add(nums[j]);
				listOfIdxList.add(list);
				if ( nums[i] < n - r + i )	{
					++nums[i];
				}	else	{
					--i;
					++nums[i];
				}
			}	else	{
				if ( nums[i] <= n - r + i )	{
					++i;
					nums[i] = nums[i - 1] + 1;
				}	else	{
					--i;
					++nums[i];
				}
			}
		}
		return	listOfIdxList;
	}

	public List<List<Integer>> getSameAveragePart(final int[] arr)	{
		int	tSum	=	0;
		for ( int i = 0; i < arr.length; ++i )	{
			tSum	+=	arr[i];
		}
		double	tAvg	=	(double) tSum / arr.length;

		for ( int n1 = 1; n1 <= arr.length / 2; ++n1 )	{
			List<List<Integer>>	listOfIdxList	=	getListOfIdxList(arr.length, n1);
			for ( List<Integer> idxList : listOfIdxList )	{
				int	sum1	=	0;
				int	sum2	=	0;
				List<Integer>	firstList	=	new ArrayList<Integer>();
				List<Integer>	secondList	=	new ArrayList<Integer>();
				for ( int i = 0; i < arr.length; ++i )	{
					if ( idxList.contains(i) )	{
						firstList.add(arr[i]);
						sum1	+=	arr[i];
					}	else	{
						secondList.add(arr[i]);
						sum2	+=	arr[i];
					}
				}
				double	avg1	=	(double) sum1 / n1;
				double	avg2	=	(double) sum2 / (arr.length - n1);
				log.debug(avg1 + " == " + avg2);
				log.debug(firstList);
				log.debug(secondList);
				if ( avg1 == avg2 )	{
					List<List<Integer>>	twoLists	=	new ArrayList<List<Integer>>(2);
					twoLists.add(firstList);
					twoLists.add(secondList);
					return	twoLists;
				}
			}
		}
		return	null;
	}

    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
