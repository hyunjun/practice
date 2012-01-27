package com.practice.interview;

import	java.util.Observable;

public class Watcher extends Observable	{
	public void action(String string)	{
		System.out.println("==========" + string + "==========");
		setChanged();
		notifyObservers(string);
	}
}

