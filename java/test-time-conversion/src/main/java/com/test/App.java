package com.test;

//	http://stackoverflow.com/questions/924208/java-how-do-you-convert-nanoseconds-to-seconds-using-the-timeunit-class
//	http://download.oracle.com/javase/6/docs/api/java/util/concurrent/TimeUnit.html
//	http://docs.oracle.com/javase/6/docs/api/java/text/SimpleDateFormat.html
//	http://www.epochconverter.com/
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class App	{
	public static long epochTime(final SimpleDateFormat sdf, final String time)	{
		try	{
			//System.out.println(sdf.toPattern());
			return	sdf.parse(time).getTime() / 1000;
		}	catch (ParseException e)	{
			System.out.println(e);
		}
		return	-1;
	}

    public static void main( String[] args ) throws Exception	{
		long	time	=	System.nanoTime();
		Thread.sleep(1243);
		long	elapsed	=	System.nanoTime() - time;
		System.out.printf("nano: %d\nmilli: %d, %d\nsec: %d, %d\n",
				elapsed,
				TimeUnit.NANOSECONDS.toMillis(elapsed),
				TimeUnit.MILLISECONDS.convert(elapsed, TimeUnit.NANOSECONDS),
				TimeUnit.NANOSECONDS.toSeconds(elapsed),
				TimeUnit.SECONDS.convert(elapsed, TimeUnit.NANOSECONDS));
    }
}
