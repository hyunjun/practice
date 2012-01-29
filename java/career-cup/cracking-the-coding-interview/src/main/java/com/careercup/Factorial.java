package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

//	20.10
public class Factorial	{

	public static List<List<Integer>> getFactorialList(final int n)	{
		if ( n < 2 )	return	null;
		List<Integer>	list	=	new ArrayList<Integer>();
		for ( int i = 0; i < n; ++i )	list.add(i);
		return	getFactorialList(n, list);
	}

	private static List<List<Integer>> getFactorialList(final int n, List<Integer> list)	{
		List<List<Integer>>	ret	=	new ArrayList<List<Integer>>();
		if ( 2 == n )	{
			List<Integer>	l1	=	new ArrayList<Integer>();
			l1.add(list.get(0));
			l1.add(list.get(1));
			List<Integer>	l2	=	new ArrayList<Integer>();
			l2.add(list.get(1));
			l2.add(list.get(0));
			ret.add(l1);
			ret.add(l2);
			return	ret;
		}

		for ( int i = 0; i < n; ++i )	{
			int	tmp	=	list.remove(i);
			int	cSize	=	ret.size();
			ret.addAll(getFactorialList(n - 1, list));
			int	nSize	=	ret.size();
			for ( int j = cSize; j < nSize; ++j )
				ret.get(j).add(0, tmp);
			list.add(i, tmp);
		}
		return	ret;
	}
}

