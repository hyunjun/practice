package com.careercup;

import static	org.junit.Assert.*;

import org.junit.*;

import	java.util.List;

public class SameAverageTest
{
	@Test
    public void testGetListOfIdxList()
	{
		SameAverage	sa	=	new SameAverage();

		List<List<Integer>>	listOfIdxList0	=	sa.getListOfIdxList(5, 1);
		assertEquals(5, listOfIdxList0.size());
		assertArrayEquals(new Integer[] { 0 }, listOfIdxList0.get(0).toArray(new Integer[1]));
		assertArrayEquals(new Integer[] { 1 }, listOfIdxList0.get(1).toArray(new Integer[1]));
		assertArrayEquals(new Integer[] { 2 }, listOfIdxList0.get(2).toArray(new Integer[1]));
		assertArrayEquals(new Integer[] { 3 }, listOfIdxList0.get(3).toArray(new Integer[1]));
		assertArrayEquals(new Integer[] { 4 }, listOfIdxList0.get(4).toArray(new Integer[1]));

		List<List<Integer>>	listOfIdxList1	=	sa.getListOfIdxList(5, 2);
		assertEquals(10, listOfIdxList1.size());
		assertArrayEquals(new Integer[] { 0, 1 }, listOfIdxList1.get(0).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 0, 2 }, listOfIdxList1.get(1).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 0, 3 }, listOfIdxList1.get(2).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 0, 4 }, listOfIdxList1.get(3).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 1, 2 }, listOfIdxList1.get(4).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 1, 3 }, listOfIdxList1.get(5).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 1, 4 }, listOfIdxList1.get(6).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 2, 3 }, listOfIdxList1.get(7).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 2, 4 }, listOfIdxList1.get(8).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 3, 4 }, listOfIdxList1.get(9).toArray(new Integer[2]));

		List<List<Integer>>	listOfIdxList2	=	sa.getListOfIdxList(5, 3);
		assertEquals(10, listOfIdxList2.size());
		assertArrayEquals(new Integer[] { 0, 1, 2 }, listOfIdxList2.get(0).toArray(new Integer[3]));
		assertArrayEquals(new Integer[] { 0, 1, 3 }, listOfIdxList2.get(1).toArray(new Integer[3]));
		assertArrayEquals(new Integer[] { 0, 1, 4 }, listOfIdxList2.get(2).toArray(new Integer[3]));
		assertArrayEquals(new Integer[] { 0, 2, 3 }, listOfIdxList2.get(3).toArray(new Integer[3]));
		assertArrayEquals(new Integer[] { 0, 2, 4 }, listOfIdxList2.get(4).toArray(new Integer[3]));
		assertArrayEquals(new Integer[] { 0, 3, 4 }, listOfIdxList2.get(5).toArray(new Integer[3]));
		assertArrayEquals(new Integer[] { 1, 2, 3 }, listOfIdxList2.get(6).toArray(new Integer[3]));
		assertArrayEquals(new Integer[] { 1, 2, 4 }, listOfIdxList2.get(7).toArray(new Integer[3]));
		assertArrayEquals(new Integer[] { 1, 3, 4 }, listOfIdxList2.get(8).toArray(new Integer[3]));
		assertArrayEquals(new Integer[] { 2, 3, 4 }, listOfIdxList2.get(9).toArray(new Integer[3]));

		List<List<Integer>>	listOfIdxList3	=	sa.getListOfIdxList(5, 4);
		assertEquals(5, listOfIdxList3.size());
		assertArrayEquals(new Integer[] { 0, 1, 2, 3 }, listOfIdxList3.get(0).toArray(new Integer[4]));
		assertArrayEquals(new Integer[] { 0, 1, 2, 4 }, listOfIdxList3.get(1).toArray(new Integer[4]));
		assertArrayEquals(new Integer[] { 0, 1, 3, 4 }, listOfIdxList3.get(2).toArray(new Integer[4]));
		assertArrayEquals(new Integer[] { 0, 2, 3, 4 }, listOfIdxList3.get(3).toArray(new Integer[4]));
		assertArrayEquals(new Integer[] { 1, 2, 3, 4 }, listOfIdxList3.get(4).toArray(new Integer[4]));
	}

	@Test
    public void testGetSameAveragePart()
	{
		SameAverage	sa	=	new SameAverage();

		List<List<Integer>>	twoLists0	=	sa.getSameAveragePart(new int[] { 10, 5, 7, 6, 2, 9, 3 });
		assertArrayEquals(new Integer[] { 6 }, twoLists0.get(0).toArray(new Integer[1]));
		assertArrayEquals(new Integer[] { 10, 5, 7, 2, 9, 3 }, twoLists0.get(1).toArray(new Integer[6]));

		List<List<Integer>>	twoLists1	=	sa.getSameAveragePart(new int[] { 2, 3, 4, 5 });
		assertArrayEquals(new Integer[] { 2, 5 }, twoLists1.get(0).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 3, 4 }, twoLists1.get(1).toArray(new Integer[2]));

		List<List<Integer>>	twoLists2	=	sa.getSameAveragePart(new int[] { 1, 2, 3, 4, 5, 15, 19 });
		assertArrayEquals(new Integer[] { 1, 5, 15 }, twoLists2.get(0).toArray(new Integer[3]));
		assertArrayEquals(new Integer[] { 2, 3, 4, 19 }, twoLists2.get(1).toArray(new Integer[4]));

		List<List<Integer>>	twoLists3	=	sa.getSameAveragePart(new int[] { 3, 12, 24, 20, 31 });
		assertArrayEquals(new Integer[] { 12, 24 }, twoLists3.get(0).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 3, 20, 31 }, twoLists3.get(1).toArray(new Integer[3]));

		List<List<Integer>>	twoLists4	=	sa.getSameAveragePart(new int[] { 19, 15, 5, 1 });
		assertArrayEquals(new Integer[] { 19, 1 }, twoLists4.get(0).toArray(new Integer[2]));
		assertArrayEquals(new Integer[] { 15, 5 }, twoLists4.get(1).toArray(new Integer[2]));

		List<List<Integer>>	twoLists5	=	sa.getSameAveragePart(new int[] { 1, 3, 5 });
		assertArrayEquals(new Integer[] { 3 }, twoLists5.get(0).toArray(new Integer[1]));
		assertArrayEquals(new Integer[] { 1, 5 }, twoLists5.get(1).toArray(new Integer[2]));
	}
}
