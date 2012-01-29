package com.practice.interview;

//	http://en.wikipedia.org/wiki/Heap_(data_structure)
//	http://coopsoft.com/ar/PriQueArticle.html
//	http://www.cprogramming.com/tutorial/computersciencetheory/heap.html
//	http://dol9.tistory.com/129
class MaxHeap
{
	private int	end;
	private int[]	data;

	public MaxHeap(final int size)	{
		end	=	0;
		data	=	new int[size];
	}

	public void add(final int n)	{
		if ( data.length - 1 == end + 1 )
			return	;

		int	pos	=	++end;
		data[pos]	=	n;
		while ( 1 < pos && data[pos / 2] < data[pos] )	{
			int	tmp	=	data[pos / 2];
			data[pos / 2]	=	data[pos];
			data[pos]	=	tmp;
			pos	/=	2;
		}
	}

	public int peek()	{
		if ( 0 < end )	return	data[1];
		return	Integer.MIN_VALUE;
	}

	public int poll()	{
		if ( 0 == end )	return	Integer.MIN_VALUE;

		int	ret	=	data[1];
		data[1]	=	data[end--];
		int	pos	=	1;
		int	chg	=	pos * 2;
		while ( pos <= end &&
			( data[pos] < data[chg] || data[pos] < data[chg + 1] ) )	{
			if ( data[chg] < data[chg + 1] )
				chg	+=	1;
			int	tmp	=	data[pos];
			data[pos]	=	data[chg];
			data[chg]	=	tmp;
			pos	=	chg;
		}
		return	ret;
	}

	public void print()	{
		if ( end == 0 )	return;
		for ( int i = 1; i <= end; ++i )
			System.out.print("\t" + data[i]);
		System.out.println();
	}
}
