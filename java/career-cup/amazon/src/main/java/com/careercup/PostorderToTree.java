package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

/**
 *	http://www.careercup.com/question?id=12493668
 */
public class PostorderToTree
{
	private static Logger	log	=	Logger.getLogger(PostorderToTree.class);

	private CharNode	root;
	public PostorderToTree()	{	root	=	null;	}

	public void create(String post, String in)	{
		if ( null == post || 0 == post.length() ||
			null == in || 0 == in.length() ||
			post.length() != in.length() )
			return;
		root	=	createNode(post, in);
	}

	private CharNode createNode(String post, String in)	{
		CharNode	n	=	new CharNode(post.charAt(post.length() - 1));

		int	split	=	0;
		for ( int i = 0; i < in.length(); ++i )
			if ( in.charAt(i) == n.getData() )	{
				split	=	i;
				break;
			}
		if ( 0 < split )
			n.setLeft(createNode(post.substring(0, split), in.substring(0, split)));
		if ( split < post.length() - 1 )
			n.setRight(createNode(post.substring(split, post.length() - 1),
					in.substring(split + 1, in.length())));

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
