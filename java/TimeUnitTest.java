//	http://stackoverflow.com/questions/924208/java-how-do-you-convert-nanoseconds-to-seconds-using-the-timeunit-class
//	http://download.oracle.com/javase/6/docs/api/java/util/concurrent/TimeUnit.html
//	http://docs.oracle.com/javase/6/docs/api/java/text/SimpleDateFormat.html
//	http://www.epochconverter.com/
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

class TimeUnitTest	{
	public static long epochTime(final SimpleDateFormat sdf, final String time)	{
		try	{
			//System.out.println(sdf.toPattern());
			return	sdf.parse(time).getTime() / 1000;
		}	catch (ParseException e)	{
			System.out.println(e);
		}
		return	-1;
	}

	public static void main(String[] args) throws Exception	{
		long	time	=	System.nanoTime();
		Thread.sleep(1243);
		long	elapsed	=	System.nanoTime() - time;
		System.out.printf("nano: %d\nmilli: %d, %d\nsec: %d, %d\n",
				elapsed,
				TimeUnit.NANOSECONDS.toMillis(elapsed),
				TimeUnit.MILLISECONDS.convert(elapsed, TimeUnit.NANOSECONDS),
				TimeUnit.NANOSECONDS.toSeconds(elapsed),
				TimeUnit.SECONDS.convert(elapsed, TimeUnit.NANOSECONDS));

		System.out.println(1136067278L == epochTime(new SimpleDateFormat("yyyy-MM-dd kk:mm:ss.SSS"), "2006-01-01 07:14:38.000"));
		System.out.println(1136041200L == epochTime(new SimpleDateFormat("yyyyMMdd"), "20060101"));
		System.out.println(1136041200L == epochTime(new SimpleDateFormat("yyMMdd"), "060101"));
		System.out.println(1311715085L == epochTime(new SimpleDateFormat("yyyy-MM-dd kk:mm:ss.SSS"), "2011-07-27 06:18:05.000"));
		System.out.println(1311715085L == epochTime(new SimpleDateFormat("yyyyMMddkkmmss"), "20110727061805"));
		System.out.println(1311715085L == epochTime(new SimpleDateFormat("yyyyMMddkkmmss"), "20110727061805"));
		System.out.println(1359359426L == epochTime(new SimpleDateFormat("EEE MMM dd kk:mm:ss Z yyyy"), "Mon Jan 28 07:50:26 +0000 2013"));	//	don't work in my mac
		System.out.println(1335761769L == epochTime(new SimpleDateFormat("yyyy-MM-dd'T'kk:mm:ss.SSSZ"), "2012-04-30T13:56:09.000+0900"));
		System.out.println(1296572903L == epochTime(new SimpleDateFormat("yyyy-MM-dd'T'kk:mm:ss.SSSZ"), "2011-02-02T00:08:23.000+0900"));
		System.out.println(1369392666L == epochTime(new SimpleDateFormat("yyyy-MM-dd'T'kk:mm:ss.SSSZ"), "2013-05-24T19:51:06.000+0900"));
	}
}

