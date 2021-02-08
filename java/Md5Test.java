import	java.io.*;
import	org.apache.commons.codec.digest.DigestUtils;

//	http://commons.apache.org/codec/api-release/index.html
//	http://stackoverflow.com/questions/304268/using-java-to-get-a-files-md5-checksum
/*
<dependency>
	<groupId>org.apache.commons</groupId>
	<artifactId>commons-codec</artifactId>
	<version>1.5</version>
</dependency>

javac -cp ~/.m2/repository/org/apache/commons/commons-codec/1.5/commons-codec-1.5.jar Md5Test.java
java -cp ~/.m2/repository/org/apache/commons/commons-codec/1.5/commons-codec-1.5.jar:. Md5Test [file path]
 */
class Md5Test	{
	public static void main(String[] args) throws Exception	{
		//System.out.println("input string: " + args[0] +
		//		"\nmd5: " + DigestUtils.md5Hex(args[0]));
		FileInputStream	fis	=	new FileInputStream(new File(args[0]));
		System.out.println("input file: " + args[0] +
				"\nmd5: " + DigestUtils.md5Hex(fis));
	}
}
