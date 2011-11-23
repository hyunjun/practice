//	http://stackoverflow.com/questions/936684/getting-the-class-name-from-a-static-method-in-java
//	http://stackoverflow.com/questions/442747/getting-the-name-of-the-current-executing-method-java
public class GetClassAndMethodName	{
	public static String getMethodName(final int depth)
	{
		final StackTraceElement[] ste = Thread.currentThread().getStackTrace();

		return ste[ste.length - 1 - depth].getMethodName();
	}

	static void testStatic()	{
		System.out.println(
			Thread.currentThread().getStackTrace()[1].getClassName() + "#" +
			//GetClassAndMethodName.class.getCanonicalName() + "#" +
			new Object(){}.getClass().getEnclosingMethod().getName() + "\n" +
			getMethodName(0) + " calls " + getMethodName(1));
	}
	void test()	{
		System.out.println(this.getClass().getSimpleName() + "#" +
			new Object(){}.getClass().getEnclosingMethod().getName() + "\n" +
			getMethodName(0) + " calls " + getMethodName(1));
	}

	public static void main(String[] args)	{
		GetClassAndMethodName.testStatic();
		new GetClassAndMethodName().test();
	}
}
