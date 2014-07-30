#	Usage

[http://maven.apache.org]

http://united-coders.com/phillip-steffensen/maven-2-part-1-setting-up-a-simple-apache-maven-2-project
http://dylankernel.tistory.com/13

mvn archetype:create -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=com.mycompany.app -DartifactId=my-app

mvn archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=com.mycompany.app -DartifactId=my-app

http://www.vineetmanohar.com/2009/11/3-ways-to-run-java-main-from-maven/
mvn exec:java -Dexec.mainClass="[main class name]" -Dexec.args="[arg0] [arg1] ..."

http://jpragmainc.wordpress.com/2011/01/28/useful-options-running-mvn-test/
mvn test -Dtest=[test name]

http://www.sonatype.com/books/mvnex-book/reference/customizing-sect-executing-tests.html

pass system properties to "maven test" task
http://www.cowtowncoder.com/blog/archives/2010/04/entry_385.html
