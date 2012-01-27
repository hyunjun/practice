package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

//	8.7
public class NCents	{
	public static int[]	UNIT	=	{ 25, 10, 5 };

	public static void print(int total)	{
		int[]	cnt	=	new int[3];
		print(total, 0, cnt);
	}
	public static void print(int total, int idx, int[] cnt)	{
		if ( 3 == idx )
			System.out.printf("25*%d + 10*%d + 5*%d + %d = %d\n",
				cnt[0], cnt[1], cnt[2], total,
				UNIT[0] * cnt[0] + UNIT[1] * cnt[1] + UNIT[2] * cnt[2] + total);
		else	{
			int	max	=	total / UNIT[idx];
			for ( int i = max; i >= 0; --i )	{
				cnt[idx]	=	i;
				print(total - UNIT[idx] * i, idx + 1, cnt);
			}
		}
	}
}

