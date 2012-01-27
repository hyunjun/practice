package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

//	8.1
public class Fibonacci	{
	public static int recur(int n)	{
		if ( n == 0 )	return	0;
		if ( n == 1 )	return	1;
		return	recur(n - 1) + recur(n - 2);
	}
	public static int iter(int n)	{
		if ( n == 0 )	return	0;
		if ( n == 1 )	return	1;
		List<Integer>	l	=	new ArrayList<Integer>();
		l.add(0);
		l.add(1);
		for ( int i = 2; i <= n; ++i )
			l.add(l.get(i - 1) + l.get(i - 2));
		return	l.get(l.size() - 1);
	}
}

