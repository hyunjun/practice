//	http://stackoverflow.com/questions/924208/java-how-do-you-convert-nanoseconds-to-seconds-using-the-timeunit-class
//	http://download.oracle.com/javase/6/docs/api/java/util/concurrent/TimeUnit.html
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

class TimeUnitTest	{
	public static long epochTimeInMin(final String format, final String time)	{
		SimpleDateFormat	sdf = new SimpleDateFormat(format);
		try	{
			Date	date = sdf.parse(time);
			return	TimeUnit.MILLISECONDS.toMinutes(date.getTime());
		}	catch (ParseException e)	{
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

		System.out.println(epochTimeInMin("yyyy-MM-dd kk:mm:ss.SSS", "2006-01-01 07:14:38.000"));
		System.out.println(epochTimeInMin("yyyyMMdd", "20060101"));
		System.out.println(epochTimeInMin("yyMMdd", "060101"));
	}
}

