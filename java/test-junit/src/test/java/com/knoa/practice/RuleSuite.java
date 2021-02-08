package com.knoa.practice;

//	http://stackoverflow.com/questions/349842/junit-4-set-up-things-in-a-test-suite-before-tests-are-run-like-a-tests-befo
//	http://weblogs.java.net/blog/johnsmart/archive/2010/04/25/grouping-tests-using-junit-categories-0
import	org.junit.*;
import	org.junit.rules.ExternalResource;
import	org.junit.runners.Suite;
import	org.junit.runner.RunWith;

@RunWith(Suite.class)
@Suite.SuiteClasses({
	RuleTest.class
})

public class RuleSuite	{
	private static int bCount = 0;
	private static int aCount = 0;

	@ClassRule
	public static ExternalResource testRule = new ExternalResource(){
		@Override
		protected void before() throws Throwable{
			System.err.println( "before test class: " + ++bCount );
			sss = "asdf";
		};

		@Override
		protected void after(){
			System.err.println( "after test class: " + ++aCount );
		};
	};

	public static String sss;
}
