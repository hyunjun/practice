package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

/**
 *	http://www.careercup.com/question?id=12477676
 */
public class PreorderToTree 
{
	private static Logger	log	=	Logger.getLogger(PreorderToTree.class);

	private CharNode	root;
	public PreorderToTree()	{	root	=	null;	}

	public void create(String s)	{
		if ( null == s || 0 == s.length() )
			return;
		root	=	createNode(s);
	}

	private CharNode createNode(String s)	{
		CharNode	n	=	null;
		switch ( s.charAt(0) )	{
			case 'L':	n	=	new CharNode('L');
						break;
			case 'N':	n	=	new CharNode('N');
						n.setLeft(createNode(s.substring(1)));
						n.setRight(createNode(s.substring(1 + n.getLeft().getLen())));
						n.setLen(n.getLen() + n.getLeft().getLen() + n.getRight().getLen());
						break;
			default:	break;
		}
		return	n;
	}

	public void traversePreorder()	{
		if ( root == null )	return;
		traversePreorder(root);
		System.out.println();
	}

	private void traversePreorder(CharNode n)	{
		System.out.print(n.getData());
		if ( n.getLeft() != null )
			traversePreorder(n.getLeft());
		if ( n.getRight() != null )
			traversePreorder(n.getRight());
	}
}

class CharNode	{
	private char	data;
	private int	len;
	private CharNode	left;
	private CharNode	right;
	public CharNode(char data)	{
		this.data	=	data;
		len	=	1;
		left	=	null;
		right	=	null;
	}
	public char getData()	{	return	this.data;	}
	public int getLen()	{	return	this.len;	}
	public void setLen(int len)	{	this.len	=	len;	}
	public void setLeft(CharNode left)	{	this.left	=	left;	}
	public CharNode getLeft()	{	return	this.left;	}
	public void setRight(CharNode right)	{	this.right	=	right;	}
	public CharNode getRight()	{	return	this.right;	}
}

