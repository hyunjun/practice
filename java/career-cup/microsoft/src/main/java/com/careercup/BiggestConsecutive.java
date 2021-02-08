package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.Map.Entry;
import	java.util.HashMap;
import	java.util.Map;

/**
 * http://www.careercup.com/question?id=13054661
 */
public class BiggestConsecutive
{
	private static Logger	log	=	Logger.getLogger(BiggestConsecutive.class);

	public static String getConsecutive(final String s)	{
		if ( null == s || 0 == s.length() )	return	null;

		//	create bit vector of characters
		int[]	arr	=	new int[26];
		for ( int i = 0; i < s.length(); ++i )
			arr[s.charAt(i) - 'a'] = 1;
		//for ( final int i : arr )	log.debug("[" + i + "]");

		//	divide groups of characters which might be consecutive
		int	j = 0, groupNum = 0;
		Map<Character, Integer>	map	=	new HashMap<Character, Integer>();
		while ( j < 26 )	{
			if ( arr[j] == 1 )	{
				while ( arr[j] == 1 )	{
					map.put((char)(j + 'a'), groupNum);
					++j;
				}
				++groupNum;
			}	else	{
				++j;
			}
		}
		/*for ( Entry<Character, Integer>	item : map.entrySet() )	{
			log.debug(String.format("map entry (%c, %d)\n", item.getKey(), item.getValue()));
		}*/
		//	if number of group is 1, return string itself because it is consecutive
		if ( groupNum == 1 )
			return	s;

		//	check substrings which has the same group number
		//	record min & max index of substring which has max length
		j = 0;
		int	minIdx = -1, tMin = -1, maxIdx = -1, tMax = -1, maxLen = -1;
		while ( j < s.length() )	{
			tMin	=	j;
			groupNum	=	map.get(s.charAt(tMin));
			//log.debug(String.format("groupNum starts at %d starting from %c\n", groupNum, s.charAt(tMin)));
			++j;
			while ( j < s.length() && groupNum == map.get(s.charAt(j)) )	{
				//log.debug(String.format("finding groupNum %d of %c(%d)\n", groupNum, s.charAt(j), j));
				++j;
			}
			//log.debug(String.format("groupNum ends at %d of %c\n", groupNum, s.charAt(j - 1)));
			tMax	=	j;
			//log.debug(String.format("substring(%d, %d) \"%s\" is group %d\n", tMin, tMax, s.substring(tMin, tMax), groupNum));
			if ( maxLen < tMax - tMin )	{
				maxLen	=	tMax - tMin;
				minIdx	=	tMin;
				maxIdx	=	tMax;
			}
		}

		return	s.substring(minIdx, maxIdx);
	}
}
