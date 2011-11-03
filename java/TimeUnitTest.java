//	http://stackoverflow.com/questions/924208/java-how-do-you-convert-nanoseconds-to-seconds-using-the-timeunit-class
//	http://download.oracle.com/javase/6/docs/api/java/util/concurrent/TimeUnit.html
import	java.util.concurrent.TimeUnit;

class TimeUnitTest	{
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
	}
}

