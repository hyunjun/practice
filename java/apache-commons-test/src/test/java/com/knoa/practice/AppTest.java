package com.knoa.practice;

import	org.junit.*;

import	java.io.*;

import org.apache.commons.configuration.XMLConfiguration;
import org.apache.commons.configuration.ConfigurationException;

public class AppTest 
{
	@BeforeClass
	public static void runBeforeClass()	{
	}

	@AfterClass
	public static void runAfterClass() {
	} 

	@Before
	public void setup() throws IOException
	{
	}

	@After
	public void teardown() throws IOException
	{
	}

	@Test
	public void testFoo1() throws IOException
	{
	}

	@Test
	public void testFoo2() throws IOException
	{
	}

	public void testConfiguration() {
		try	{
			XMLConfiguration config = new XMLConfiguration(getClass().getClassLoader().getResource("main-config.xml"));

			Assert.assertEquals("config 0", config.getString("main.config(0)"));
			Assert.assertEquals("config 1", config.getString("main.config(1)"));
			Assert.assertEquals("config 2", config.getString("main.config(2)"));
			Assert.assertEquals("something else in main-config", config.getString("main.else"));
			Assert.assertEquals("some config in main-config", config.getString("something"));

			config = new XMLConfiguration(getClass().getClassLoader().getResource("test-config.xml"));

			Assert.assertEquals("config a", config.getString("test.config(0)"));
			Assert.assertEquals("config b", config.getString("test.config(1)"));
			Assert.assertEquals("config c", config.getString("test.config(2)"));
			Assert.assertEquals("something else in test-config", config.getString("test.else"));
			Assert.assertEquals("some config in test-config", config.getString("something"));
		}       catch (ConfigurationException e)        {
			System.out.println(e);
		}
	}
}
