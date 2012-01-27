package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class DecoratorTest	{
	@Test
	public void testDecorator()	{
		Decorator	decorator	=	new Decorator();
		System.out.println(decorator.getName());
		Decorator	child	=	new ChildDecorator(decorator);
		System.out.println(child.getName());
		Decorator	child2	=	new ChildDecorator(child);
		System.out.println(child2.getName());
	}
}
