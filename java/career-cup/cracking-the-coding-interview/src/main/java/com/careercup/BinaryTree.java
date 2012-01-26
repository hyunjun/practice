package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.List;

public class BinaryTree
{
	public class TCNode	{
		private int	data;
		private TCNode	left;
		private TCNode	right;
		private TCNode	parent;
		public TCNode(final int data)	{
			this.data	=	data;
			this.left	=	null;
			this.right	=	null;
			this.parent	=	null;
		}
		public int getData()	{	return this.data;	}
		public void setData(final int data)	{	this.data	=	data;	}
		public TCNode getLeft()	{	return	this.left;	}
		public void setLeft(final TCNode left)	{	this.left	=	left;	}
		public TCNode getRight()	{	return	this.right;	}
		public void setRight(final TCNode right)	{	this.right	=	right;	}
		public TCNode getParent()	{	return	this.parent;	}
		public void setParent(final TCNode parent)	{	this.parent	=	parent;	}
		public String toString()	{	return	"[" + data + "]";	}
	}

	//private Logger	log	=	Logger.getLogger(this.getClass());
	private Logger	log	=	Logger.getLogger(BinaryTree.class);

	private TCNode	root;

	public BinaryTree()	{
		root	=	null;
	}
	public BinaryTree(int data)	{
		root	=	new TCNode(data);
	}

	//	4.1	tree is balanced or not
	private int getDepth(TCNode n)	{
		if ( n == null )
			return	0;
		if ( n.getLeft() == null && n.getRight() == null )
			return	1;
		int	left = 0, right = 0;
		if ( n.getLeft() != null )	left	=	getDepth(n.getLeft());
		if ( n.getRight() != null )	right	=	getDepth(n.getRight());
		return	Math.max(left, right) + 1;
	}
	public boolean isBalanced()	{
		int	left = 0, right = 0;
		if ( root.getLeft() != null )	left	=	getDepth(root.getLeft());
		if ( root.getRight() != null )	right	=	getDepth(root.getRight());
		if ( Math.abs(left - right) < 2 )
			return	true;
		return	false;
	}

	public int getDepth()	{
		return	getDepth(root);
	}

	//	4.3	change increasing sorted array into minimal height binary tree
	public void createBTFromArray(final int[] arr)	{
		TCNode[]	nodes	=	new TCNode[arr.length];
		for ( int i = 0; i < arr.length; ++i )
			nodes[i]	=	new TCNode(arr[i]);
		root	=	nodes[0];
		for ( int i = 0; i < arr.length; ++i )	{
			if ( 2 * i + 1 < arr.length )
				nodes[i].setLeft(nodes[2 * i + 1]);
			if ( 2 * i + 2 < arr.length )
				nodes[i].setRight(nodes[2 * i + 2]);
		}
	}

	//	4.4	create linked list from binary search tree
	public class LNode   {
		private int data;
		private LNode    next;
		public LNode(final int data) {   this.data   =   data;   }
		public int getData()    {   return  this.data;  }
		public void setNext(final LNode next)    {   this.next   =   next;   }
		public LNode getNext()   {   return  this.next;  }
		public String toString()	{	return	"[" + data + "]";	}
	}

	public void print(LNode cNode) {
		System.out.print("head");
		while ( null != cNode )   {
			System.out.print(" -> " + cNode.getData());
			cNode   =   cNode.getNext();
		}
		System.out.println(" -> end");
	}

	public void createLL()	{
		List<LNode>	list	=	new ArrayList<LNode>();
		Integer	depth	=	new Integer(0);
		createLL(root, depth, list);
		for ( LNode n : list )
			print(n);
	}

	private void createLL(TCNode tn, Integer depth, List<LNode> lnList)	{
		++depth;
		LNode	head	=	lnList.size() < depth ? null : lnList.get(depth - 1);
		if ( null == head )	{
			head	=	new LNode(tn.getData());
			head.setNext(null);
			lnList.add(head);
		}	else	{
			LNode	ln	=	head;
			while ( null != ln.getNext() )
				ln	=	ln.getNext();
			ln.setNext(new LNode(tn.getData()));
		}
		if ( tn.getLeft() != null )
			createLL(tn.getLeft(), depth, lnList);
		if ( tn.getRight() != null )
			createLL(tn.getRight(), depth, lnList);
		--depth;
	}

	//	4.5	find next node as inroder successor. link to parent node exists
	public TCNode getNext(int data)	{
		List<TCNode>	nList	=	new ArrayList<TCNode>();
		nList.add(root);
		TCNode	t	=	null;
		while ( nList.size() > 0 )	{
			TCNode	c	=	nList.remove(0);
			if ( c.getData() == data )	{
				t	=	c;
				break;
			}
			if ( c.getLeft() != null )	nList.add(c.getLeft());
			if ( c.getRight() != null )	nList.add(c.getRight());
		}
		if ( null == t )	return	null;

		if ( t.equals(root) )	{
			TCNode	next	=	t.getRight();
			while ( next.getLeft() != null )	next	=	next.getLeft();
			return	next;
		}

		boolean	isLeft	=	(t.getParent().getLeft() != null && t.getParent().getLeft().equals(t)) ? true : false;
		boolean	hasLeft	=	t.getLeft() != null ? true : false;
		boolean	hasRight	=	t.getRight() != null ? true : false;
		if ( isLeft && ( ( !hasLeft && !hasRight ) || ( hasLeft && !hasRight ) ) )
			return	t.getParent();
		if ( !isLeft && ( ( !hasLeft && !hasRight ) || ( hasLeft && !hasRight ) ) )	{
			TCNode	next	=	t.getParent();
			while ( null != next && null != next.getParent() && next.getParent().getRight().equals(next) )	{
				next	=	next.getParent();
			}
			return	next == null ? next : next.getParent();
		}
		if ( hasRight )	{
			TCNode	next	=	t.getRight();
			while ( next.getLeft() != null )	next	=	next.getLeft();
			return	next;
		}
		return	null;
	}

	//	4.6	first common ancestor of two nodes in binary tree. avoid storing additional nodes
	private boolean searchNode(TCNode n, int a)	{
		if ( n.getData() == a )	return	true;
		if ( n.getLeft() != null )
			if ( searchNode(n.getLeft(), a) )
				return	true;
		if ( n.getRight() != null )
			if ( searchNode(n.getRight(), a) )
				return	true;
		return	false;
	}
	private void findCA(TCNode n, int a, int b, TCNode ca)	{
		Boolean	foundA	=	false;
		Boolean	foundB	=	false;
		if ( n.getLeft() != null )	{
			if ( !foundA )
				foundA	=	searchNode(n.getLeft(), a);
			if ( !foundB )
				foundB	=	searchNode(n.getLeft(), b);
			if ( foundA && foundB )
				findCA(n.getLeft(), a, b, ca);
		}
		if ( n.getRight() != null )	{
			if ( !foundA )
				foundA	=	searchNode(n.getRight(), a);
			if ( !foundB )
				foundB	=	searchNode(n.getRight(), b);
			if ( foundA && foundB )
				findCA(n.getRight(), a, b, ca);
		}
		if ( foundA && foundB && ca.getData() == Integer.MIN_VALUE )	{
			ca.setData(n.getData());
		}
		//System.out.println("visited " + n.getData());
	}
	public int findCA(int a, int b)	{
		if ( root == null )	return	Integer.MIN_VALUE;
		TCNode	ca	=	new TCNode(Integer.MIN_VALUE);
		findCA(root, a, b, ca);
		return	ca.getData();
	}

	//	4.8	print all paths which sum up to the value
	private void findPath(TCNode n, List<TCNode> pathList, int sum)	{
		pathList.add(n);
		int	tmp	=	0;
		for ( TCNode x : pathList )	tmp	+=	x.getData();
		if ( sum == tmp )
			System.out.println(pathList);
		if ( n.getLeft() != null )	findPath(n.getLeft(), pathList, sum);
		if ( n.getRight() != null )	findPath(n.getRight(), pathList, sum);
		pathList.remove(pathList.size() - 1);
	}
	public void findPath(int sum)	{
		List<TCNode>	pathList	=	new ArrayList<TCNode>();
		findPath(root, pathList, sum);
	}

	//////////////////////
	//	basic features	//
	//////////////////////
	public TCNode search(final int data)	{
		TCNode	cNode	=	root;
		List<TCNode>	list	=	new ArrayList<TCNode>();
		while ( cNode.getData() != data )	{
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

	public boolean insertLeft(final int target, final int data)	{
		return	insert(target, true, data);
	}

	public boolean insertRight(final int target, final int data)	{
		return	insert(target, false, data);
	}

	public boolean insert(final int target, final boolean isLeft, final int data)	{
		TCNode	tNode	=	search(target);
		if ( null == tNode.getLeft() && true == isLeft )	{
			TCNode	nNode	=	new TCNode(data);
			tNode.setLeft(nNode);
			nNode.setParent(tNode);
			log.debug(String.format("insert %d into left of %d <- %d", data, tNode.getLeft().getData(), tNode.getData()));
			return	true;
		}
		if ( null == tNode.getRight() && false == isLeft )	{
			TCNode	nNode	=	new TCNode(data);
			tNode.setRight(nNode);
			nNode.setParent(tNode);
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

	public boolean remove(final int data)	{
		TCNode	pNode	=	null;
		TCNode	cNode	=	root;
		List<TCNode>	pList	=	new ArrayList<TCNode>();
		List<TCNode>	list	=	new ArrayList<TCNode>();
		while ( cNode.getData() != data )	{
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
				TCNode	leafParentNode	=	pNode;
				TCNode	leafNode	=	cNode;
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
				TCNode	leafParentNode	=	pNode;
				TCNode	leafNode	=	cNode;
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
	private void traverseInorder(final TCNode node)	{
		if ( null != node.getLeft() )
			traverseInorder(node.getLeft());
		System.out.printf("[%d]", node.getData());
		if ( null != node.getRight() )
			traverseInorder(node.getRight());
	}

	public void traversePreorder()	{
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
}
