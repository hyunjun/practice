package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.HashMap;
import	java.util.HashSet;
import	java.util.Map;
import	java.util.Map.Entry;
import	java.util.Set;

/**
 * http://www.careercup.com/question?id=13072668
 */
public class ArrayGraph 
{
	private static Logger	log	=	Logger.getLogger(ArrayGraph.class);

	public static int getHeight(final int[] nodes)	{
		int[]	heights	=	new int[nodes.length];
		int	i = 0, j = 0, prev = 0, maxHeight = 0;
		while ( i < nodes.length )	{
			j	=	i;
			prev	=	0;
			while ( heights[j] == 0 ||
					( 0 != heights[j] && heights[j] < prev + 1 ) )	{
				heights[j]	=	++prev;
				//	if current node's parent is root
				if ( -1 == nodes[j] )	{
					if ( maxHeight < heights[j] )	{
						maxHeight	=	heights[j];
					}
					break;
				}
				j	=	nodes[j];
			}
			++i;
		}
		return	maxHeight;
	}

	public static int getHeight1(final int[] nodes)	{
		Map<Integer, Set<Integer>>	map	=	new HashMap<Integer, Set<Integer>>();
		for ( int i = 0; i < nodes.length; ++i )	{
			Set<Integer>	set	=	map.get(nodes[i]);
			if ( null == set )	set	=	new HashSet<Integer>();
			set.add(i);
			map.put(nodes[i], set);
		}
		for ( Entry<Integer, Set<Integer>> item : map.entrySet() )
			log.debug(String.format("%d > %s", item.getKey(), item.getValue()));
		return	map.keySet().size();
	}
}
