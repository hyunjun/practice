package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.HashSet;
import	java.util.Iterator;
import	java.util.Set;

//	8.3
public class Subset	{
	public Set<Set<Integer>> getSubset(Set<Integer> s)	{
		Set<Set<Integer>>	ss	=	new HashSet<Set<Integer>>();
		ss.add(s);
		for ( Iterator<Integer> itr = s.iterator(); itr.hasNext(); )	{
			Set<Integer>	tmp	=	new HashSet<Integer>(s);
			tmp.remove(itr.next());
			ss.addAll(getSubset(tmp));
		}
		return	ss;
	}
}

