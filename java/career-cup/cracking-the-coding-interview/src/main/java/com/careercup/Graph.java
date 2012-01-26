package com.careercup;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.Collections;
import	java.util.List;

public class Graph
{
	private Logger	log	=	Logger.getLogger(this.getClass());

	public class Vertex	{
		private int	data;
		private List<Vertex>	edgeList;
		private boolean	visited;
		public Vertex(final int data)	{
			this.data	=	data;
			edgeList	=	new ArrayList<Vertex>();
			visited	=	false;
		}
		public void setData(final int data)	{	this.data	=	data;	}
		public int getData()	{	return	this.data;	}
		public void addEdge(final Vertex v)	{
			if ( null != v && false == edgeList.contains(v) )
				edgeList.add(v);
		}
		public Vertex getEdge(final int data)	{
			for ( final Vertex v : edgeList )
				if ( v.getData() == data )
					return	v;
			return	null;
		}
		public List<Vertex> getEdges()	{
			return	Collections.unmodifiableList(edgeList);
		}
		public void setVisited(final boolean visited)	{	this.visited	=	visited;	}
		public boolean isVisited()	{	return	visited;	}
	}

	private Vertex	root	=	null;

	public Graph()	{}

	//	4.2	is there route between two nodes?
	public boolean hasRoute()	{
		List<Vertex>	list	=	new ArrayList<Vertex>();
		list.add(root);
		while ( list.size() > 0 )	{
			Vertex	c	=	list.remove(0);
			c.setVisited(true);
			for ( Vertex t : c.getEdges() )	{
				if ( t.isVisited() )	return	true;
				else					list.add(t);
			}
		}
		return	false;
	}

	public void addEdge(final int srcData, final int dstData)	{
		if ( null == root )
			root	=	new Vertex(srcData);
		Vertex	srcV	=	bfs(srcData);
		if ( null == srcV )	return;
		Vertex	dstV	=	bfs(dstData);
		if ( null == dstV )	dstV	=	new Vertex(dstData);
		srcV.addEdge(dstV);
		log.debug("add edge " + srcData + " -> " + dstData);
	}

	public Vertex bfs(final int data)	{
		if ( null == root )	return	null;
		Vertex	curV	=	root;
		List<Vertex>	uvList	=	new ArrayList<Vertex>();	//	unvisited
		List<Vertex>	vList	=	new ArrayList<Vertex>();	//	visited
		while ( curV.getData() != data )	{
			vList.add(curV);
			List<Vertex>	edgeList	=	curV.getEdges();
			for ( final Vertex edge : edgeList )	{
				if ( false == vList.contains(edge) && false == uvList.contains(edge) )	{
					uvList.add(edge);
				}
			}
			if ( 0 == uvList.size() )	return	null;
			curV	=	uvList.remove(0);
		}
		if ( log.isDebugEnabled() )	{
			StringBuffer	sb	=	new StringBuffer("visited: ");
			for ( final Vertex v : vList )
				sb.append(" -> " + v.getData());
			log.debug(sb.toString());
		}
		return	curV;
	}

	public Vertex dfs(final int data)	{
		if ( null == root )	return	null;
		Vertex	curV	=	root;
		List<Vertex>	uvList	=	new ArrayList<Vertex>();	//	unvisited
		List<Vertex>	vList	=	new ArrayList<Vertex>();	//	visited
		while ( curV.getData() != data )	{
			vList.add(curV);
			List<Vertex>	edgeList	=	curV.getEdges();
			for ( int i = edgeList.size() - 1; i >= 0; --i )	{
				Vertex	edge	=	edgeList.get(i);
				if ( false == vList.contains(edge) && false == uvList.contains(edge) )	{
					uvList.add(0, edge);
				}
			}
			if ( 0 == uvList.size() )	return	null;
			curV	=	uvList.remove(0);
		}
		if ( log.isDebugEnabled() )	{
			StringBuffer	sb	=	new StringBuffer("visited: ");
			for ( final Vertex v : vList )
				sb.append(" -> " + v.getData());
			log.debug(sb.toString());
		}
		return	curV;
	}

	public void bfs()	{
		Vertex	curV	=	root;
		List<Vertex>	uvList	=	new ArrayList<Vertex>();	//	unvisited
		List<Vertex>	vList	=	new ArrayList<Vertex>();	//	visited
		while ( null != curV )	{
			vList.add(curV);
			List<Vertex>	edgeList	=	curV.getEdges();
			for ( final Vertex edge : edgeList )	{
				if ( false == vList.contains(edge) && false == uvList.contains(edge) )	{
					uvList.add(edge);
				}
			}
			if ( 0 == uvList.size() )	break;
			curV	=	uvList.remove(0);
		}
		StringBuffer	sb	=	new StringBuffer("visited: ");
		for ( final Vertex v : vList )
			sb.append(" -> " + v.getData());
		log.info(sb.toString());
	}

	//	http://www.algolist.net/Algorithms/Graph/Undirected/Depth-first_search
	public void dfs()	{
		Vertex	curV	=	root;
		List<Vertex>	uvList	=	new ArrayList<Vertex>();	//	unvisited
		List<Vertex>	vList	=	new ArrayList<Vertex>();	//	visited
		while ( null != curV )	{
			vList.add(curV);
			List<Vertex>	edgeList	=	curV.getEdges();
			for ( int i = edgeList.size() - 1; i >= 0; --i )	{
				Vertex	edge	=	edgeList.get(i);
				if ( false == vList.contains(edge) && false == uvList.contains(edge) )	{
					uvList.add(0, edge);
				}
			}
			if ( 0 == uvList.size() )	break;
			curV	=	uvList.remove(0);
		}
		StringBuffer	sb	=	new StringBuffer("visited: ");
		for ( final Vertex v : vList )
			sb.append(" -> " + v.getData());
		log.info(sb.toString());
	}
}
