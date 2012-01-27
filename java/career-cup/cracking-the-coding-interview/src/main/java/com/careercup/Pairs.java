package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

//	8.5
public class Pairs	{
	public void print(int n)	{
		print(new ArrayList<Character>(), n, n);
	}
	private void print(List<Character> list, int open, int close)	{
		if ( open == 0 && close == 0 )	{
			for ( Character c : list )	System.out.print(c);
			System.out.println();
		}
		if ( 0 < open )	{
			List<Character>	tmpList	=	new ArrayList<Character>();
			tmpList.addAll(list);
			tmpList.add('(');
			print(tmpList, open - 1, close);
		}
		if ( open < close )	{
			List<Character>	tmpList	=	new ArrayList<Character>();
			tmpList.addAll(list);
			tmpList.add(')');
			print(tmpList, open, close - 1);
		}
	}
}

