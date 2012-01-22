package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.List;

public class PrimeTest
{
	@Test
    public void testPrime()
	{
		assertEquals(true, Prime.isPrimeBasic(2));
		assertEquals(true, Prime.isPrimeBasic(3));
		assertEquals(false, Prime.isPrimeBasic(4));
		assertEquals(true, Prime.isPrimeBasic(5));
		assertEquals(false, Prime.isPrimeBasic(6));
		assertEquals(true, Prime.isPrimeBasic(7));
		assertEquals(false, Prime.isPrimeBasic(8));
		assertEquals(false, Prime.isPrimeBasic(9));
		assertEquals(false, Prime.isPrimeBasic(10));
		assertEquals(true, Prime.isPrimeBasic(11));
		assertEquals(false, Prime.isPrimeBasic(12));
		assertEquals(true, Prime.isPrimeBasic(13));
		assertEquals(false, Prime.isPrimeBasic(14));
		assertEquals(false, Prime.isPrimeBasic(15));
		assertEquals(false, Prime.isPrimeBasic(16));
		assertEquals(true, Prime.isPrimeBasic(17));
		assertEquals(false, Prime.isPrimeBasic(18));
		assertEquals(true, Prime.isPrimeBasic(19));
		assertEquals(false, Prime.isPrimeBasic(20));
		assertEquals(true, Prime.isPrimeBasic(541));
		assertEquals(true, Prime.isPrimeBasic(105943));	//	http://www.bigprimes.net/archive/prime/101/

		assertEquals(true, Prime.isPrime(2));
		assertEquals(true, Prime.isPrime(3));
		assertEquals(false, Prime.isPrime(4));
		assertEquals(true, Prime.isPrime(5));
		assertEquals(false, Prime.isPrime(6));
		assertEquals(true, Prime.isPrime(7));
		assertEquals(false, Prime.isPrime(8));
		assertEquals(false, Prime.isPrime(9));
		assertEquals(false, Prime.isPrime(10));
		assertEquals(true, Prime.isPrime(11));
		assertEquals(false, Prime.isPrime(12));
		assertEquals(true, Prime.isPrime(13));
		assertEquals(false, Prime.isPrime(14));
		assertEquals(false, Prime.isPrime(15));
		assertEquals(false, Prime.isPrime(16));
		assertEquals(true, Prime.isPrime(17));
		assertEquals(false, Prime.isPrime(18));
		assertEquals(true, Prime.isPrime(19));
		assertEquals(false, Prime.isPrime(20));
		assertEquals(true, Prime.isPrime(541));
		assertEquals(true, Prime.isPrime(105943));
	}
}
