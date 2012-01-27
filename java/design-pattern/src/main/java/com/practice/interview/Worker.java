package com.practice.interview;

//	http://iilii.egloos.com/3806897
public abstract class Worker	{
	protected abstract void doit();
	public final void work()	{
		System.out.println("start");
		doit();
		System.out.println("end");
	}
}
