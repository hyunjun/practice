package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

//	8.4
public class Permutation	{
	public List<String> getStrPerm(String s)	{
		List<String>	list	=	new ArrayList<String>();
		for ( int i = 0; i < s.length(); ++i )	{
			StringBuilder	sb	=	new StringBuilder(s);
			char	first	=	sb.charAt(i);
			sb.deleteCharAt(i);
			if ( sb.length() == 1 )
				list.add(first + sb.toString());
			else	{
				List<String>	tmpList	=	getStrPerm(sb.toString());
				for ( String r : tmpList )
					list.add(first + r);
			}
		}
		return	list;
	}
}

