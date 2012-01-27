package com.practice.interview;

public class ChildDecorator extends Decorator	{
	private Decorator	decorator;
	public ChildDecorator(Decorator decorator)	{
		this.decorator	=	decorator;
	}
	@Override
	public String getName()	{
		return	"@" + decorator.getName() + "@";
	}
}
