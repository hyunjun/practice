package com.knoa.practice;

import	org.junit.*;

import	java.io.*;

//	http://stackoverflow.com/questions/2597271/easy-to-get-a-test-file-into-junit
public class AppTest 
{
	private BufferedReader in = null;

	@Before
	public void setup() throws IOException
	{
		in	=	new BufferedReader(
					new InputStreamReader(
						getClass().getClassLoader().getResourceAsStream(
							"test-resource.txt")));
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
	public void testFoo() throws IOException
	{
		String line = in.readLine();

		Assert.assertNotNull(line);
	}
}
