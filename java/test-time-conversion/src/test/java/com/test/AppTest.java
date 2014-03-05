package com.test;

import java.text.SimpleDateFormat;
import java.text.ParseException;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

//	http://commons.apache.org/proper/commons-lang/userguide.html
//	http://commons.apache.org/proper/commons-lang/javadocs/api-release/org/apache/commons/lang3/time/FastDateFormat.html
import org.apache.commons.lang3.time.FastDateFormat;	

public class AppTest extends TestCase	{
	//	thread unsafe
    public void testSimpleDateFormat()	{
		assertEquals(1136067278L, App.epochTime(new SimpleDateFormat("yyyy-MM-dd kk:mm:ss.SSS"), "2006-01-01 07:14:38.000"));
		assertEquals(1136041200L, App.epochTime(new SimpleDateFormat("yyyyMMdd"), "20060101"));
		assertEquals(1136041200L, App.epochTime(new SimpleDateFormat("yyMMdd"), "060101"));
		assertEquals(1311715085L, App.epochTime(new SimpleDateFormat("yyyy-MM-dd kk:mm:ss.SSS"), "2011-07-27 06:18:05.000"));
		assertEquals(1311715085L, App.epochTime(new SimpleDateFormat("yyyyMMddkkmmss"), "20110727061805"));
		assertEquals(1311715085L, App.epochTime(new SimpleDateFormat("yyyyMMddkkmmss"), "20110727061805"));
		//assertEquals(1359359426L, App.epochTime(new SimpleDateFormat("EEE MMM dd kk:mm:ss Z yyyy"), "Mon Jan 28 07:50:26 +0000 2013"));	//	don't work in my mac
		assertEquals(1335761769L, App.epochTime(new SimpleDateFormat("yyyy-MM-dd'T'kk:mm:ss.SSSZ"), "2012-04-30T13:56:09.000+0900"));
		assertEquals(1296572903L, App.epochTime(new SimpleDateFormat("yyyy-MM-dd'T'kk:mm:ss.SSSZ"), "2011-02-02T00:08:23.000+0900"));
		assertEquals(1369392666L, App.epochTime(new SimpleDateFormat("yyyy-MM-dd'T'kk:mm:ss.SSSZ"), "2013-05-24T19:51:06.000+0900"));
    }

	//	thread safe
    public void testFastDateFormat() throws ParseException	{
		assertEquals(1136067278L, FastDateFormat.getInstance("yyyy-MM-dd kk:mm:ss.SSS").parse("2006-01-01 07:14:38.000").getTime() / 1000);
		assertEquals(1136041200L, FastDateFormat.getInstance("yyyyMMdd").parse("20060101").getTime() / 1000);
		assertEquals(1136041200L, FastDateFormat.getInstance("yyMMdd").parse("060101").getTime() / 1000);
		assertEquals(1311715085L, FastDateFormat.getInstance("yyyy-MM-dd kk:mm:ss.SSS").parse("2011-07-27 06:18:05.000").getTime() / 1000);
		assertEquals(1311715085L, FastDateFormat.getInstance("yyyyMMddkkmmss").parse("20110727061805").getTime() / 1000);
		assertEquals(1311715085L, FastDateFormat.getInstance("yyyyMMddkkmmss").parse("20110727061805").getTime() / 1000);
		//assertEquals(1359359426L, FastDateFormat.getInstance("EEE MMM dd kk:mm:ss Z yyyy").parse("Mon Jan 28 07:50:26 +0000 2013").getTime() / 1000);	//	don't work in my mac
		assertEquals(1335761769L, FastDateFormat.getInstance("yyyy-MM-dd'T'kk:mm:ss.SSSZ").parse("2012-04-30T13:56:09.000+0900").getTime() / 1000);
		assertEquals(1296572903L, FastDateFormat.getInstance("yyyy-MM-dd'T'kk:mm:ss.SSSZ").parse("2011-02-02T00:08:23.000+0900").getTime() / 1000);
		assertEquals(1369392666L, FastDateFormat.getInstance("yyyy-MM-dd'T'kk:mm:ss.SSSZ").parse("2013-05-24T19:51:06.000+0900").getTime() / 1000);
    }
}
