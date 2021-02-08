import	java.io.*;

//	http://stackoverflow.com/questions/1277880/how-can-i-get-the-count-of-line-in-a-file-in-an-efficient-way
class GetLineTest	{
	public static void main(String[] args) throws IOException	{
		LineNumberReader	reader	=	null;
		try {
			reader	=	new LineNumberReader(new FileReader(args[0]));
			while ( ( reader.readLine() ) != null );
			System.out.println("total line: " +	reader.getLineNumber());
		}	finally	{
			if ( reader != null )	reader.close();
		}
	}
}
