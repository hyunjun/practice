package com.practice.interview;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

//	http://groups.engin.umd.umich.edu/CIS/course.des/cis350/treetool/help/help.html
//	http://groups.engin.umd.umich.edu/CIS/course.des/cis350/treetool/index.html
public class BinarySearchTree
{
	public class TCNode	{
		private int	data;
		private TCNode	left;
		private TCNode	right;
		public TCNode(final int data)	{
			setData(data);
			setLeft(null);
			setRight(null);
		}
		public int getData()	{	return this.data;	}
		public void setData(final int data)	{	this.data	=	data;	}
		public TCNode getLeft()	{	return	this.left;	}
		public void setLeft(final TCNode left)	{	this.left	=	left;	}
		public TCNode getRight()	{	return	this.right;	}
		public void setRight(final TCNode right)	{	this.right	=	right;	}
	}

	//private Logger	log	=	Logger.getLogger(this.getClass());
	private Logger	log	=	Logger.getLogger(BinarySearchTree.class);

	private TCNode	root;

	public BinarySearchTree()	{
		root	=	null;
	}

	public boolean isEmpty()	{
		return	root == null ? true : false;
	}

	public TCNode search(final int data)	{
		TCNode	cNode	=	root;
		if ( isEmpty() )	return	null;
		int	cmp	=	0;
		while ( cNode != null )	{
			if ( cNode.getData() > data )	{
				cNode	=	cNode.getLeft();
			}	else if ( cNode.getData() < data )	{
				cNode	=	cNode.getRight();
			}	else	{
				log.debug(String.format("return found Node(%d)", cNode.getData()));
				return	cNode;
			}
		}
		return	null;
	}

	public void insert(final int data)	{
		if ( isEmpty() )	{
			root	=	new TCNode(data);
			return;
		}
		TCNode	pNode	=	null;
		TCNode	cNode	=	root;
		while ( cNode != null )	{
			pNode	=	cNode;
			if ( cNode.getData() > data )	{
				cNode	=	cNode.getLeft();
			}	else if ( cNode.getData() < data )	{
				cNode	=	cNode.getRight();
			}	else	{
				return;
			}
		}
		cNode	=	new TCNode(data);
		if ( pNode.getData() > data )
			pNode.setLeft(cNode);
		else
			pNode.setRight(cNode);
	}

	public void traverseInorder()	{
		if ( isEmpty() )	return;
		traverseInorder(root);
		System.out.println();
	}
	private void traverseInorder(final TCNode node)	{
		if ( null != node.getLeft() )
			traverseInorder(node.getLeft());
		System.out.printf("[%d]", node.getData());
		if ( null != node.getRight() )
			traverseInorder(node.getRight());
	}

	public void traversePreorder()	{
		if ( isEmpty() )	return;
		traversePreorder(root);
		System.out.println();
	}
	private void traversePreorder(final TCNode node)	{
		System.out.printf("[%d]", node.getData());
		if ( null != node.getLeft() )
			traversePreorder(node.getLeft());
		if ( null != node.getRight() )
			traversePreorder(node.getRight());
	}

	public void traversePostorder()	{
		if ( isEmpty() )	return;
		traversePostorder(root);
		System.out.println();
	}
	private void traversePostorder(final TCNode node)	{
		if ( null != node.getLeft() )
			traversePostorder(node.getLeft());
		if ( null != node.getRight() )
			traversePostorder(node.getRight());
		System.out.printf("[%d]", node.getData());
	}

	/*
	public boolean remove(int data)	{
		if ( isEmpty() )	return	false;

		//	search node to remove
		TCNode	pNode	=	null;
		TCNode	cNode	=	root;
		boolean	isCNodeLeft	=	true;
		while ( cNode != null )	{
			pNode	=	cNode;
			if ( cNode.getData() > data )	{
				cNode	=	cNode.getLeft();
				isCNodeLeft	=	true;
			}	else if ( cNode.getData() < data )	{
				cNode	=	cNode.getRight();
				isCNodeLeft	=	false;
			}	else
				break;
		}
		if ( cNode == null )	return	false;

		TCNode	left	=	cNode.getLeft();
		TCNode	right	=	cNode.getRight();
		//	when removing root
		if ( cNode.equals(root) )	{
			if ( left == null && right == null )	{
				root	=	null;
			}	else if ( left != null && right == null )	{
				root	=	left;
				cNode	=	null;
			}	else if ( left == null && right != null )	{
				root	=	right;
				cNode	=	null;
			}	else	{
				TCNode	promoteParent	=	left;
				TCNode	promote	=	left.getRight();
				while ( promote.getLeft() != null || promote.getRight() != null )	{
					promoteParent	=	promote;
					promote	=	promote.getRight();
				}
				promote.setLeft(left);
				promote.setRight(right);
				root	=	promote;
				promoteParent.setRight(null);
				cNode	=	null;
			}
		}	else	{
			if ( left == null && right == null )	{
				cNode	=	null;
			}	else if ( left != null && right == null )	{
				if ( isCNodeLeft )	pNode.setLeft(left);
				else				pNode.setRight(left);
				cNode	=	null;
			}	else if ( left == null && right != null )	{
				if ( isCNodeLeft )	pNode.setLeft(right);
				else				pNode.setRight(right);
				cNode	=	null;
			}	else	{
				if ( left.getRight() == null )	{
					if ( isCNodeLeft )	pNode.setLeft(left);
					else				pNode.setRight(left);
					left.setRight(right);
					cNode	=	null;
				}	else	{
					TCNode	promoteParent	=	left;
					TCNode	promote	=	left.getRight();
					while ( promote.getLeft() != null || promote.getRight() != null )	{
						promoteParent	=	promote;
						promote	=	promote.getRight();
					}
					promote.setLeft(left);
					promote.setRight(right);
					promoteParent.setRight(null);
					if ( isCNodeLeft )	pNode.setLeft(promote);
					else				pNode.setRight(promote);
					cNode	=	null;
				}
			}
		}

		return	true;
	}
	*/
}
