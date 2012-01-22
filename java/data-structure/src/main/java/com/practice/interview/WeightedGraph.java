package com.practice.interview;

import	org.apache.log4j.Logger;

import	java.util.ArrayList;
import	java.util.Collections;
import	java.util.List;

public class WeightedGraph<T>
{
	private Logger	log	=	Logger.getLogger(this.getClass());

	public class Vertex<T>	{
		private T	data;
		private List<Vertex<T>>	edgeList;
		public Vertex(final T data)	{
			this.data	=	data;
			edgeList	=	new ArrayList<Vertex<T>>();
		}
		public void setData(final T data)	{	this.data	=	data;	}
		public T getData()	{	return	this.data;	}
		public void addEdge(final Vertex<T> v)	{
			if ( null != v && false == edgeList.contains(v) )
				edgeList.add(v);
		}
		public Vertex<T> getEdge(final T data)	{
			for ( final Vertex<T> v : edgeList )
				if ( v.getData().equals(data) )
					return	v;
			return	null;
		}
		public List<Vertex<T>> getEdges()	{
			return	Collections.unmodifiableList(edgeList);
		}
	}

	public class Edge<T>	{
		private Vertex<T>	v1, v2;
		private int	weight;
		public Edge<T>(final Vertex<T> v1, final Vertex<T> v2, final int weight)	{
			this.v1	=	v1;
			this.v2	=	v2;
			this.weight	=	weight;
		}
		public int getWeight()	{	return	this.weight;	}
		public boolean hasSameVertices(final Edge<T> edge)	{
			final Vertex<T>	v1	=	edge.getVertex1();
			final Vertex<T>	v2	=	edge.getVertex2();
			if ( ( v1.getData().equals(v1.getData()) && v2.getData().equals(v2.getData()) ) ||
				( v1.getData().equals(v2.getData()) && v2.getData().equals(v1.getData()) ) )
				return	true;
			return	false;
		}
	}

	private Vertex<T>	root	=	null;

	public WeightedGraph()	{}

	public void addEdge(final T srcData, final T dstData)	{
		if ( null == root )
			root	=	new Vertex<T>(srcData);
		Vertex<T>	srcV	=	bfs(srcData);
		if ( null == srcV )	return;
		Vertex<T>	dstV	=	bfs(dstData);
		if ( null == dstV )	dstV	=	new Vertex<T>(dstData);
		srcV.addEdge(dstV);
		log.debug("add edge " + srcData + " -> " + dstData);
	}

	public Vertex<T> bfs(final T data)	{
		if ( null == root )	return	null;
		Vertex<T>	curV	=	root;
		List<Vertex<T>>	uvList	=	new ArrayList<Vertex<T>>();	//	unvisited
		List<Vertex<T>>	vList	=	new ArrayList<Vertex<T>>();	//	visited
		while ( false == curV.getData().equals(data) )	{
			vList.add(curV);
			List<Vertex<T>>	edgeList	=	curV.getEdges();
			for ( final Vertex<T> edge : edgeList )	{
				if ( false == vList.contains(edge) && false == uvList.contains(edge) )	{
					uvList.add(edge);
				}
			}
			if ( 0 == uvList.size() )	return	null;
			curV	=	uvList.remove(0);
		}
		if ( log.isDebugEnabled() )	{
			StringBuffer	sb	=	new StringBuffer("visited: ");
			for ( final Vertex<T> v : vList )
				sb.append(" -> " + v.getData());
			log.debug(sb.toString());
		}
		return	curV;
	}

	public Vertex<T> dfs(final T data)	{
		if ( null == root )	return	null;
		Vertex<T>	curV	=	root;
		List<Vertex<T>>	uvList	=	new ArrayList<Vertex<T>>();	//	unvisited
		List<Vertex<T>>	vList	=	new ArrayList<Vertex<T>>();	//	visited
		while ( false == curV.getData().equals(data) )	{
			vList.add(curV);
			List<Vertex<T>>	edgeList	=	curV.getEdges();
			for ( int i = edgeList.size() - 1; i >= 0; --i )	{
				Vertex<T>	edge	=	edgeList.get(i);
				if ( false == vList.contains(edge) && false == uvList.contains(edge) )	{
					uvList.add(0, edge);
				}
			}
			if ( 0 == uvList.size() )	return	null;
			curV	=	uvList.remove(0);
		}
		if ( log.isDebugEnabled() )	{
			StringBuffer	sb	=	new StringBuffer("visited: ");
			for ( final Vertex<T> v : vList )
				sb.append(" -> " + v.getData());
			log.debug(sb.toString());
		}
		return	curV;
	}

	public void bfs()	{
		Vertex<T>	curV	=	root;
		List<Vertex<T>>	uvList	=	new ArrayList<Vertex<T>>();	//	unvisited
		List<Vertex<T>>	vList	=	new ArrayList<Vertex<T>>();	//	visited
		while ( null != curV )	{
			vList.add(curV);
			List<Vertex<T>>	edgeList	=	curV.getEdges();
			for ( final Vertex<T> edge : edgeList )	{
				if ( false == vList.contains(edge) && false == uvList.contains(edge) )	{
					uvList.add(edge);
				}
			}
			if ( 0 == uvList.size() )	break;
			curV	=	uvList.remove(0);
		}
		StringBuffer	sb	=	new StringBuffer("visited: ");
		for ( final Vertex<T> v : vList )
			sb.append(" -> " + v.getData());
		log.info(sb.toString());
	}

	//	http://www.algolist.net/Algorithms/Graph/Undirected/Depth-first_search
	public void dfs()	{
		Vertex<T>	curV	=	root;
		List<Vertex<T>>	uvList	=	new ArrayList<Vertex<T>>();	//	unvisited
		List<Vertex<T>>	vList	=	new ArrayList<Vertex<T>>();	//	visited
		while ( null != curV )	{
			vList.add(curV);
			List<Vertex<T>>	edgeList	=	curV.getEdges();
			for ( int i = edgeList.size() - 1; i >= 0; --i )	{
				Vertex<T>	edge	=	edgeList.get(i);
				if ( false == vList.contains(edge) && false == uvList.contains(edge) )	{
					uvList.add(0, edge);
				}
			}
			if ( 0 == uvList.size() )	break;
			curV	=	uvList.remove(0);
		}
		StringBuffer	sb	=	new StringBuffer("visited: ");
		for ( final Vertex<T> v : vList )
			sb.append(" -> " + v.getData());
		log.info(sb.toString());
	}
}
