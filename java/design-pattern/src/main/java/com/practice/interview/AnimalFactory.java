package com.practice.interview;

//	http://iilii.egloos.com/3791596
public class AnimalFactory	{
	public static Animal create(String animalName)	{
		if ( null == animalName )	{
			throw new IllegalArgumentException("name is null");
		}
		if ( animalName.equals("cow") )	{
			return	new Cow();
		}	else if ( animalName.equals("cat") )	{
			return	new Cat();
		}	else if ( animalName.equals("dog") )	{
			return	new Dog();
		}	else	{
			return	null;
		}
	}
}

