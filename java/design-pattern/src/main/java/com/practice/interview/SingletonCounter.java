package com.practice.interview;

//	http://iilii.egloos.com/3807664
public class SingletonCounter	{
	public static SingletonCounter	singleton	=	new SingletonCounter();
	private int	cnt	=	0;
	private SingletonCounter()	{}
	public static SingletonCounter getInstance()	{
		return	singleton;
	}
	public int getNextInt()	{
		return	++cnt;
	}
}

class SingletonCounter2	{
	private static SingletonCounter2	singleton;
	private int	cnt	=	0;
	private SingletonCounter2()	{}
	public static synchronized SingletonCounter2 getInstance()	{
		if ( singleton == null )
			singleton	=	new SingletonCounter2();
		return	singleton;
	}
	public int getNextInt()	{
		return	++cnt;
	}
}

class SingletonCounter3	{
	private volatile static SingletonCounter3	singleton;
	private int	cnt	=	0;
	private SingletonCounter3()	{}
	public static SingletonCounter3 getInstance()	{
		if ( singleton == null )	{
			synchronized(SingletonCounter3.class)	{
				if ( singleton == null )	{
					singleton	=	new SingletonCounter3();
				}
			}
		}
		return	singleton;
	}
	public int getNextInt()	{
		return	++cnt;
	}
}

class SingletonCounter4	{
	private static class SingletonHolder	{
		static final SingletonCounter4	singleton	=	new SingletonCounter4();
	}
	private int	cnt	=	0;
	private SingletonCounter4()	{}
	public static SingletonCounter4 getInstance()	{
		return	SingletonHolder.singleton;
	}
	public int getNextInt()	{
		return	++cnt;
	}
}
