package com.knoa.practice;

import	org.junit.*;

import	java.io.*;

//	http://stackoverflow.com/questions/2597271/easy-to-get-a-test-file-into-junit
public class AppTest 
{
	private static String	fileName;
	private BufferedReader in = null;

	//	http://www.cavdar.net/2008/07/21/junit-4-in-60-seconds/
	@BeforeClass
	public static void runBeforeClass()	{
		//	run for one time before all test cases
		fileName	=	"test-resource.txt";
	}

	@AfterClass
	public static void runAfterClass() {
		//	run for one time after all test cases
		fileName	=	null;
	} 

	@Before
	public void setup() throws IOException
	{
		in	=	new BufferedReader(
					new InputStreamReader(
						getClass().getClassLoader().getResourceAsStream(
							fileName)));
	}

	@After
	public void teardown() throws IOException
	{
		if (in != null)	{
			in.close();
		}
		in = null;
	}

	@Test
	public void testFoo1() throws IOException
	{
		String line = in.readLine();

		Assert.assertNotNull(line);
	}

	@Test
	public void testFoo2() throws IOException
	{
		String line = in.readLine();

		Assert.assertNotNull(line);
	}
}
