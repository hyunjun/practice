package com.practice.interview;

import	java.util.Observable;
import	java.util.Observer;

public class Spy implements Observer	{
	private Employee	employee;
	public Spy(Employee employee)	{
		this.employee	=	employee;
	}
	public void update(Observable o, Object arg)	{
		if ( o instanceof Watcher )	{
			System.out.println("Spy let us know " + employee.getDesc() + " is playing");
		}
	}
}

