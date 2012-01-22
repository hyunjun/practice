package com.practice.interview;

import static	org.junit.Assert.*;

import org.junit.*;

public class WeightedGraphTest
{
	@Test
    public void testBfs()	{
		WeightedGraph<Character>	g	=	new WeightedGraph<Character>();
		g.addEdge('A', 'B');
		g.addEdge('A', 'C');
		g.addEdge('A', 'D');
		g.addEdge('B', 'E');
		g.addEdge('C', 'F');
		g.addEdge('D', 'F');
		g.addEdge('E', 'G');
		g.addEdge('F', 'G');
		assertEquals(Character.valueOf('A'), g.bfs('A').getData());
		assertEquals(Character.valueOf('B'), g.bfs('B').getData());
		assertEquals(Character.valueOf('C'), g.bfs('C').getData());
		assertEquals(Character.valueOf('D'), g.bfs('D').getData());
		assertEquals(Character.valueOf('E'), g.bfs('E').getData());
		assertEquals(Character.valueOf('F'), g.bfs('F').getData());
		assertEquals(Character.valueOf('G'), g.bfs('G').getData());
		g.bfs();
    }

	@Test
    public void testDfs()	{
		WeightedGraph<Character>	g	=	new WeightedGraph<Character>();
		g.addEdge('A', 'B');
		g.addEdge('A', 'C');
		g.addEdge('A', 'D');
		g.addEdge('B', 'E');
		g.addEdge('C', 'F');
		g.addEdge('D', 'F');
		g.addEdge('E', 'G');
		g.addEdge('F', 'G');
		assertEquals(Character.valueOf('A'), g.dfs('A').getData());
		assertEquals(Character.valueOf('B'), g.dfs('B').getData());
		assertEquals(Character.valueOf('C'), g.dfs('C').getData());
		assertEquals(Character.valueOf('D'), g.dfs('D').getData());
		assertEquals(Character.valueOf('E'), g.dfs('E').getData());
		assertEquals(Character.valueOf('F'), g.dfs('F').getData());
		assertEquals(Character.valueOf('G'), g.dfs('G').getData());
		g.dfs();
    }
}
