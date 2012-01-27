package com.practice.interview;

import	java.util.ArrayList;
import	java.util.Iterator;
import	java.util.List;

//	http://iilii.egloos.com/3788564
public class IteratorPattern implements Iterable<String>	{
	private List<String>	list	=	new ArrayList<String>();

	public void add(String name)	{
		list.add(name);
	}

	public Iterator<String> iterator()	{
		return	new Iterator<String>()	{
			int	seq	=	0;
			public boolean hasNext()	{
				return	seq < list.size();
			}
			public String next()	{
				return	list.get(seq++);
			}
			public void remove()	{
				throw new UnsupportedOperationException();
			}
		};
	}

    public static void main( String[] args )
    {
		IteratorPattern	ip	=	new IteratorPattern();
		ip.add("AAA");
		ip.add("BBB");
		ip.add("CCC");

		Iterator<String>	itr	=	ip.iterator();
		while ( itr.hasNext() )	{
			System.out.println(itr.next());
		}
    }
}

