package com.careercup;

/**
 *	http://www.careercup.com/question?id=12468661
 */
public class SumOfThreeNumbers
{
	public SumOfThreeNumbers(){}

	public int[] getArrays(final int[] array)	{
		if ( array.length < 3 )
			return	null;

		int	start	=	0;
		int	mid	=	start + 1;
		int	end	=	array.length - 1;
		boolean	found	=	false;
		while ( start + 1 < end )	{
			//System.out.printf("loop start\t%d\t%d\t%d\n", array[start], array[mid], array[end]);
			int	partSum	=	array[start] + array[end];
			int	target	=	0 - partSum;
			found	=	false;
			for ( mid = start + 1; mid < end; ++mid )	{
				//System.out.printf("\tmid = %d, array[%d] = %d\n", mid, mid, array[mid]);
				if ( target < array[mid] )
					break;
				if ( target == array[mid] )	{
					found	=	true;
					break;
				}
			}
			//System.out.printf("after inner loop\t%d\t%d\t%d\n", array[start], array[mid], array[end]);
			if ( found )	break;
			if ( 0 < partSum )	--end;
			else				++start;
		}
		//System.out.printf("%d\t%d\t%d\n", array[start], array[mid], array[end]);
		return	new int[] { array[start], array[mid], array[end] };
	}

    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
