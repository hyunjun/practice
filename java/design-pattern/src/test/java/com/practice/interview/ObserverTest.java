package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class ObserverTest	{
	@Test
	public void testObserver()	{
		Watcher	watcher	=	new Watcher();
		Employee	pc1	=	new Employee("watching comcis");
		Employee	pc2	=	new Employee("sleeping");
		Employee	pc3	=	new Employee("playing poker");
		Spy	spy	=	new Spy(pc3);

		watcher.addObserver(pc1);
		watcher.addObserver(pc2);
		watcher.addObserver(pc3);
		watcher.addObserver(spy);

		watcher.action("boss comes");
		watcher.deleteObserver(pc3);
		watcher.deleteObserver(spy);

		watcher.action("boss leaves");
	}
}
