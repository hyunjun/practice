package com.careercup;

/**
 *	http://www.careercup.com/question?id=12469661
 */
public class ComparisonOfTwoArrays 
{
	public int[]	arr1;
	public int[]	arr2;
	public int[]	res;

	public ComparisonOfTwoArrays(final int[] arr1, final int[] arr2)	{
		this.arr1	=	new int[arr1.length];
		for ( int i = 0; i < arr1.length; ++i )
			this.arr1[i]	=	arr1[i];
		this.arr2	=	new int[arr2.length];
		for ( int i = 0; i < arr2.length; ++i )
			this.arr2[i]	=	arr2[i];
		this.res	=	new int[100];
	}

	public void compare()	{
		int[]	tmp1	=	new int[100];
		for ( int i = 0; i < arr1.length; ++i )	{
			if ( arr1[i] != 0 )
				tmp1[arr1[i]]	=	1;
		}
		int[]	tmp2	=	new int[100];
		for ( int i = 0; i < arr2.length; ++i )	{
			if ( arr2[i] != 0 )
				tmp2[arr2[i]]	=	1;
		}

		for ( int i = 0; i < res.length; ++i )	{
			res[i]	=	tmp1[i] & tmp2[i];
		}
	}

	public void print(final int lastIdx)	{
		for ( int i = 0; i < arr1.length; ++i )	{
			if ( 0 != arr1[i] )	System.out.printf("%3d", arr1[i]);
			else				System.out.printf("  0");
		}
		System.out.println();
		for ( int i = 0; i < arr2.length; ++i )	{
			if ( 0 != arr2[i] )	System.out.printf("%3d", arr2[i]);
			else				System.out.printf("  0");
		}
		System.out.println();
		for ( int i = 0; i < lastIdx; ++i )	{
			System.out.printf("%3d", res[i]);
		}
		System.out.println();
	}

    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
