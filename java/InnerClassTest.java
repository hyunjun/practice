public class InnerClassTest	{
	public static void main(final String[] args)	{
		Outer.StaticInner	obj0	=	new Outer.StaticInner();
		obj0.f();
		Outer.Inner	obj1	=	new Outer().new Inner();
		obj1.f();
	}
}

//	http://www.brpreiss.com/books/opus5/html/page601.html
//	http://alecture.blogspot.com/2011/05/inner-classes.html
class Outer	{
	int	y;
	public static class StaticInner	{
		int	x;

		void f(){}
	}

	public class Inner	{
		int	x;

		void f(){}
	}
}
