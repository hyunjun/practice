package com.practice.interview;

//	http://iilii.egloos.com/5378691
public class Panel	{
	private String	color	=	"RED";
	public String getColor()	{
		return	color;
	}
	public void setColor(String color)	{
		System.out.println("change from " + this.color + " into " + color);
		this.color	=	color;
	}
}

