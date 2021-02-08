package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.ArrayList;
import	java.util.Enumeration;
import	java.util.List;

public class SingletonTest
{
	public void a()	{
		SingletonCounter	sc	=	SingletonCounter.getInstance();
		System.out.println("method a counter " + sc.getNextInt());

		SingletonCounter2	sc2	=	SingletonCounter2.getInstance();
		System.out.println("method a counter " + sc2.getNextInt());

		SingletonCounter3	sc3	=	SingletonCounter3.getInstance();
		System.out.println("method a counter " + sc3.getNextInt());

		SingletonCounter4	sc4	=	SingletonCounter4.getInstance();
		System.out.println("method a counter " + sc4.getNextInt());
	}
	public void b()	{
		SingletonCounter	sc	=	SingletonCounter.getInstance();
		System.out.println("method b counter " + sc.getNextInt());

		SingletonCounter2	sc2	=	SingletonCounter2.getInstance();
		System.out.println("method b counter " + sc2.getNextInt());

		SingletonCounter3	sc3	=	SingletonCounter3.getInstance();
		System.out.println("method b counter " + sc3.getNextInt());

		SingletonCounter4	sc4	=	SingletonCounter4.getInstance();
		System.out.println("method b counter " + sc4.getNextInt());
	}

	@Test
    public void testFactory()
    {
		SingletonTest	st	=	new SingletonTest();
		st.a();
		st.b();
    }
}
