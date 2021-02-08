package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

/**
 *	http://www.careercup.com/question?id=12342686
 */
public class Prime
{
	private static Logger	log	=	Logger.getLogger(Prime.class);

	public static boolean isPrimeBasic(final int n)	{
		if ( n <= 1 )	return	false;
		if ( n <= 3 )	return	true;
		for ( int i = 2; i <= n / 2; ++i )	{
			//log.debug(n + " % " + i + " => " + n % i);
			if ( n % i == 0 )	return	false;
		}
		return	true;
	}

	public static boolean isPrime(int n) {
		if ( n <= 1 )	return	false;
		if ( n <= 3 )	return	true;

		if ( n % 2 == 0 )	return	false;
		if ( n % 3 == 0 )	return	false;

		int	squareRootOfN	=	(int) Math.sqrt(n);
		int	x	=	5;

		while ( x <= squareRootOfN )	{
			if ( n % x == 0 )	return	false;
			x +=	2;
			if ( n % x == 0 )	return	false;
			x +=	4;
		}
		return true;
	}
}
