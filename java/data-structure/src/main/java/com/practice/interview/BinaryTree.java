package com.practice.interview;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

//	Generic BinaryTree
//	See Effective Java, 2nd edition, Item 26
//	http://groups.engin.umd.umich.edu/CIS/course.des/cis350/treetool/help/help.html
//	http://groups.engin.umd.umich.edu/CIS/course.des/cis350/treetool/index.html
public class BinaryTree<T>
{
	public class TCNode<T>	{
		private T	data;
		private TCNode<T>	left;
		private TCNode<T>	right;
		public TCNode(final T data)	{
			this.data	=	data;
			this.left	=	null;
			this.right	=	null;
		}
		public T getData()	{	return this.data;	}
		public void setData(final T data)	{	this.data	=	data;	}
		public TCNode<T> getLeft()	{	return	this.left;	}
		public void setLeft(final TCNode<T> left)	{	this.left	=	left;	}
		public TCNode<T> getRight()	{	return	this.right;	}
		public void setRight(final TCNode<T> right)	{	this.right	=	right;	}
	}

	//private Logger	log	=	Logger.getLogger(this.getClass());
	private Logger	log	=	Logger.getLogger(BinaryTree.class);

	private TCNode<T>	root;

	public BinaryTree(T data)	{
		root	=	new TCNode<T>(data);
		root.setLeft(null);
		root.setRight(null);
	}

	public TCNode<T> search(final T data)	{
		TCNode<T>	cNode	=	root;
		List<TCNode<T>>	list	=	new ArrayList<TCNode<T>>();
		while ( false == cNode.getData().equals(data) )	{
			if ( null != cNode.getLeft() )	list.add(cNode.getLeft());
			if ( null != cNode.getRight() )	list.add(cNode.getRight());
			if ( 0 == list.size() )	{
				log.debug(String.format("no such Node(%d)", data));
				return	null;
			}
			cNode	=	list.remove(0);
		}
		log.debug(String.format("return found Node(%d)", cNode.getData()));
		return	cNode;
	}

	public boolean insertLeft(final T target, final T data)	{
		return	insert(target, true, data);
	}

	public boolean insertRight(final T target, final T data)	{
		return	insert(target, false, data);
	}

	public boolean insert(final T target, final boolean isLeft, final T data)	{
		TCNode<T>	tNode	=	search(target);
		if ( null == tNode.getLeft() && true == isLeft )	{
			tNode.setLeft(new TCNode<T>(data));
			log.debug(String.format("insert %d into left of %d <- %d", data, tNode.getLeft().getData(), tNode.getData()));
			return	true;
		}
		if ( null == tNode.getRight() && false == isLeft )	{
			tNode.setRight(new TCNode<T>(data));
			log.debug(String.format("insert %d into right of %d -> %d", data, tNode.getData(), tNode.getRight().getData()));
			return	true;
		}
		if ( log.isDebugEnabled() )	{
			if ( null == tNode )
				log.debug(String.format("can NOT insert %d because %d doesn't exist", data, target));
			else
				log.debug(String.format("can NOT insert %d into left or right of %d", data, tNode.getData()));
		}
		return	false;
	}

	public boolean delete(final T data)	{
		TCNode<T>	pNode	=	null;
		TCNode<T>	cNode	=	root;
		List<TCNode<T>>	pList	=	new ArrayList<TCNode<T>>();
		List<TCNode<T>>	list	=	new ArrayList<TCNode<T>>();
		while ( false == cNode.getData().equals(data) )	{
			if ( null != cNode.getLeft() )	{
				pList.add(cNode);
				list.add(cNode.getLeft());
			}
			if ( null != cNode.getRight() )	{
				pList.add(cNode);
				list.add(cNode.getRight());
			}
			if ( 0 == list.size() )	{
				log.debug(String.format("no such Node(%d)", data));
				return	false;
			}
			pNode	=	pList.remove(0);
			cNode	=	list.remove(0);
		}
		if ( pNode.getLeft().equals(cNode) )	{
			if ( null == cNode.getLeft() && null == cNode.getRight() )	{
				pNode.setLeft(null);
			}	else	{
				TCNode<T>	leafParentNode	=	pNode;
				TCNode<T>	leafNode	=	cNode;
				while ( false == ( null == leafNode.getLeft() && null == leafNode.getRight() ) )	{
					if ( null != leafNode.getRight() )	{
						leafParentNode	=	leafNode;
						leafNode	=	leafNode.getRight();
					}
					if ( null != leafNode.getLeft() )	{
						leafParentNode	=	leafNode;
						leafNode	=	leafNode.getLeft();
					}
				}
				if ( leafParentNode.getLeft().equals(leafNode) )
					leafParentNode.setLeft(null);
				else if ( leafParentNode.getRight().equals(leafNode) )
					leafParentNode.setRight(null);
				pNode.setLeft(leafNode);
				leafNode.setLeft(cNode.getLeft());
				leafNode.setRight(cNode.getRight());
			}
			cNode	=	null;
		}	else if ( pNode.getRight().equals(cNode) )	{
			if ( null == cNode.getLeft() && null == cNode.getRight() )	{
				pNode.setRight(null);
			}	else	{
				TCNode<T>	leafParentNode	=	pNode;
				TCNode<T>	leafNode	=	cNode;
				while ( false == ( null == leafNode.getLeft() && null == leafNode.getRight() ) )	{
					if ( null != leafNode.getRight() )	{
						leafParentNode	=	leafNode;
						leafNode	=	leafNode.getRight();
					}
					if ( null != leafNode.getLeft() )	{
						leafParentNode	=	leafNode;
						leafNode	=	leafNode.getLeft();
					}
				}
				if ( leafParentNode.getLeft().equals(leafNode) )
					leafParentNode.setLeft(null);
				else if ( leafParentNode.getRight().equals(leafNode) )
					leafParentNode.setRight(null);
				pNode.setRight(leafNode);
				leafNode.setLeft(cNode.getLeft());
				leafNode.setRight(cNode.getRight());
			}
			cNode	=	null;
		}
		return	true;
	}

	public void traverseInorder()	{
		traverseInorder(root);
		System.out.println();
	}
	private void traverseInorder(final TCNode<T> node)	{
		if ( null != node.getLeft() )
			traverseInorder(node.getLeft());
		if ( null != node.getData() )
			System.out.printf("[%d]", node.getData());
		if ( null != node.getRight() )
			traverseInorder(node.getRight());
	}

	public void traversePreorder()	{
		traversePreorder(root);
		System.out.println();
	}
	private void traversePreorder(final TCNode<T> node)	{
		if ( null != node.getData() )
			System.out.printf("[%d]", node.getData());
		if ( null != node.getLeft() )
			traversePreorder(node.getLeft());
		if ( null != node.getRight() )
			traversePreorder(node.getRight());
	}

	public void traversePostorder()	{
		traversePostorder(root);
		System.out.println();
	}
	private void traversePostorder(final TCNode<T> node)	{
		if ( null != node.getLeft() )
			traversePostorder(node.getLeft());
		if ( null != node.getRight() )
			traversePostorder(node.getRight());
		if ( null != node.getData() )
			System.out.printf("[%d]", node.getData());
	}

    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
