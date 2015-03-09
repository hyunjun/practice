package	com.knoa.practice;

import static	org.junit.Assert.*;

import	org.junit.ClassRule;
import	org.junit.Rule;
import	org.junit.Test;
import	org.junit.rules.ExternalResource;
import	org.junit.runner.RunWith;

//	this must be run by RuleSuite
//	mvn test -Dtest=RuleSuite	OK
//	mvn test	Error
public class RuleTest	{
	@Test
	public void asdf1(){
		assertNotNull("A value should've been set by a rule.", RuleSuite.sss);
	}

	@Test
	public void asdf2(){
		assertEquals("This value should be set by the rule.", "asdf", RuleSuite.sss);
	}
}
