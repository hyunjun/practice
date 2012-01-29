package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.HashSet;
import	java.util.Iterator;
import	java.util.Set;

//	20.4
public class NumOfTwos	{

	private static int getTwo(int n)	{
		if ( 0 == n || 1 == n )	return	0;
		int	divide = 1, num = 1;
		while ( Math.pow(10, num) < n )	{	++num;	divide *= 10;	}
		int	res	=	0;
		while ( 1 <= divide )	{
			int	c	=	n / divide;
			if ( 2 == c )	++res;
			n	-=	c * divide;
			divide	/=	10;
		}
		return	res;
	}

	public static int getNumOfTwo(int n)	{
		int	sum	=	0;
		for ( int i = 2; i <= n; ++i )	{
			sum	+=	getTwo(i);
		}
		return	sum;
	}

	public static int count2sR(int n)	{
		//	Base case
		if ( n == 0 )	return	0;

		//	513 into 5 * 100 + 13.[Power = 100; First = 5; Remainder = 13]
		int	power	=	1;
		while ( 10 * power < n )	power *= 10;
		int	first	=	n / power;
		int	remainder	=	n % power;
		//	Count 2s from first digit
		int	nTwosFirst	=	0;
		if ( first > 2 )	nTwosFirst	+=	power;
		else if ( first == 2 )	nTwosFirst	+=	remainder + 1;

		//	Count 2s from all other digits
		int	nTwosOther	=	first * count2sR(power - 1) + count2sR(remainder);

		return	nTwosFirst + nTwosOther;
	}

	public static int count2sI(int num)	{
		int	countof2s = 0, digit = 0;
		int	j = num, seendigits = 0, position = 0, pow10_pos = 1;
		while ( j > 0 )	{
			digit	=	j % 10;
			int	pow10_posMinus1	=	pow10_pos / 10;
			countof2s +=	digit * position * pow10_posMinus1;
			if ( digit == 2 )	{
				countof2s	+=	seendigits + 1;
			}
			else if ( digit > 2 )	{
				countof2s	+=	pow10_pos;
			}
			seendigits	=	seendigits + pow10_pos * digit;
			pow10_pos	*=	10;
			position++;
			j	=	j / 10;
		}
		return	countof2s;
	}
}

