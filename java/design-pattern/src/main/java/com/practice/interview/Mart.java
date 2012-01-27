package com.practice.interview;

public class Mart	{
	private Seller	seller;
	public Mart(Seller seller)	{
		this.seller	=	seller;
	}
	public void order()	{
		seller.sell();
	}
}

