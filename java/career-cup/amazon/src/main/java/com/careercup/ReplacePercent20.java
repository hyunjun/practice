package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

/**
 *	http://www.careercup.com/question?id=13032664
 */
public class ReplacePercent20
{
	private static Logger	log	=	Logger.getLogger(ReplacePercent20.class);

	public static String replace(final String s) {
		StringBuilder	sb	=	new StringBuilder(s);
		int	len	=	sb.length();
		int	j = 0;
		int	num	=	0;
		for ( int i = 0; j < len; ++i, ++j )	{
			sb.setCharAt(i, sb.charAt(j));
			if ( sb.charAt(i) == '%' )	{
				if ( sb.charAt(i + 1) == '2'
					&& sb.charAt(i + 2) == '0' )	{
					sb.setCharAt(i, ' ');
					j	=	i + 2;
					++num;
				}
			}
			log.debug(sb.substring(0, i));
		}
		log.debug(String.format("j = %d\tlen = %d\n", j, len));
		if ( j - 2 * num < len )	{
			sb.delete(j - 2 * num, len);
		}
		log.debug(sb.toString());
		return	sb.toString();
	}
}
