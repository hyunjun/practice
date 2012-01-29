package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.HashSet;
import	java.util.Iterator;
import	java.util.Set;

//	20.1
public class Add	{
	public static int add(int a, int b)	{
		int	bit = 0, left = 0, right = 0, res = 0;
		for ( int i = 0; i < 31; ++i )	{
			bit	=	0x1 << i;
			left	=	a & bit;
			if ( 0 < left )	{
				//System.out.println("bit = " + bit + "\tres = " + res + "\tres & bit = " + (res & bit) + "\tleft = " + left);
				if ( 0 < (res & bit) )	{
					res	^=	bit;
					res	|=	bit << 1;
					//System.out.println("\tleft 1\tbit = " + bit + "\tres = " + res);
				}	else	{
					res	|=	bit;
					//System.out.println("\tleft 2\tbit = " + bit + "\tres = " + res);
				}
			}
			right	=	b & bit;
			if ( 0 < right )	{
				//System.out.println("bit = " + bit + "\tres = " + res + "\tres & bit = " + (res & bit) + "\tright = " + right);
				if ( 0 < (res & bit) )	{
					res	^=	bit;
					res	|=	bit << 1;
					//System.out.println("\tright 1\tbit = " + bit + "\tres = " + res);
				}	else	{
					res	|=	bit;
					//System.out.println("\tright 2\tbit = " + bit + "\tres = " + res);
				}
			}
			//System.out.println("\tcurrent res = " + res);
		}
		//System.out.println("res = " + res);
		return	res;
	}

	public static int add_no_arithm(int a, int b)	{
		if ( b == 0 )	return	a;
		int	sum	=	a ^ b;	//	add without carrying
		int	carry	=	(a & b) << 1;	//	carry, but don't add
		return	add_no_arithm(sum, carry);	//	recurse
	}
}

