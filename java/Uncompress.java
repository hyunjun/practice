import	java.io.File;
import	java.io.FileInputStream;
import	java.io.FileOutputStream;
import	java.io.FileNotFoundException;
import	java.io.InputStream;
import	java.io.IOException;
import	java.util.Enumeration;
import	java.util.zip.GZIPInputStream;
import	java.util.zip.ZipEntry;
import	java.util.zip.ZipException;
import	java.util.zip.ZipInputStream;

import	org.apache.commons.compress.archivers.ArchiveEntry;
import	org.apache.commons.compress.archivers.tar.TarArchiveInputStream;
import	org.apache.commons.compress.archivers.zip.ZipArchiveEntry;
import	org.apache.commons.compress.archivers.zip.ZipFile;
//import	org.apache.commons.compress.compressors.bzip2.BZip2CompressorInputStream;

//import	org.apache.hadoop.io.compress.bzip2.CBZip2InputStream;

/*
 * javac -cp ~/.m2/repository/org/apache/commons/commons-compress/1.2/commons-compress-1.2.jar Uncompress.java
 * java -cp ~/.m2/repository/org/apache/commons/commons-compress/1.2/commons-compress-1.2.jar:. Uncompress [file name].[tar.gz | zip]
 */
public class Uncompress	{
	public static void main(final String[] args)	{
		if ( 1 != args.length || null == args[0] || 0 == args[0].length() )
			return;

		if ( args[0].endsWith(".tar.gz") )	{
			uncompressTarGz(args[0]);
		//}	else if ( args[0].endsWith(".tar.bz2") )	{
		//	uncompressTarBz2(args[0]);
		}	else if ( args[0].endsWith(".zip") )	{
			uncompressZip(args[0]);
		}	else	{
			System.out.println("unsupported type");
		}
	}

	private static byte[] getBytes(InputStream is, long size) throws Exception {
		if ( size > Integer.MAX_VALUE ) {
			throw new Exception("A file is too large.");
		}
		int	length	=	(int)size;
		byte[]	bytes	=	new byte[length];
		int	offset	=	0;
		int	numRead	=	0;

		while ( offset < bytes.length &&
			( numRead = is.read(bytes, offset, bytes.length - offset) ) >= 0 ) {
			offset += numRead;
		}

		if ( offset < bytes.length ) {
			throw new IOException("A file could not be completely read.");
		}

		return bytes;
	}

	public static void uncompressTarGz(final String filePath)	{
		InputStream	is	=	null;
		FileInputStream	fis	=	null;
		try {
			fis =   new FileInputStream(new File(filePath));
			is  =   new GZIPInputStream(fis);
		}   catch (FileNotFoundException fnfe)  {
			System.out.println(fnfe.getMessage());
		}   catch (IOException ioe) {
			System.out.println(ioe.getMessage());
		}
		TarArchiveInputStream	tais    =   new TarArchiveInputStream(is);
		try {
			ArchiveEntry    entry   =   null;
			while ( ( entry = tais.getNextEntry() ) != null ) {
				if ( entry.isDirectory() )  {   continue;   }
				final String    fileName    =   entry.getName();
				byte[]  bytes    =   getBytes(tais, entry.getSize());

				final FileOutputStream	fos	=	new FileOutputStream(fileName);
				fos.write(bytes);
				fos.close();
			}
		}   catch (IOException ioe) {
			System.out.println("IOException\t" + ioe.getMessage());
		}	catch (Exception e)	{
			System.out.println(e.getMessage());
		}   finally {
			try	{
				if ( null != is )   is.close();
				if ( null != tais ) tais.close();
			}	catch (IOException ioe)	{
			}
		}
	}

	/*
	public static void uncompressTarBz2(final String filePath)	{
		InputStream	is	=	null;
		FileInputStream	fis	=	null;
		try {
			fis =   new FileInputStream(new File(filePath));
			//is  =   new BZip2CompressorInputStream(fis);
			fis.skip(2);
			is  =   new CBZip2InputStream(fis);
		}   catch (FileNotFoundException fnfe)  {
			System.out.println(fnfe.getMessage());
		}   catch (IOException ioe) {
			System.out.println(ioe.getMessage());
		}
		TarArchiveInputStream	tais    =   new TarArchiveInputStream(is);
		try {
			ArchiveEntry    entry   =   null;
			while ( ( entry = tais.getNextEntry() ) != null ) {
				if ( entry.isDirectory() )  {   continue;   }
				final String    fileName    =   entry.getName();
				byte[]  data    =   getBytes(tais, entry.getSize());

				final FileOutputStream	fos	=	new FileOutputStream(fileName);
				fos.write(data);
			}
		}   catch (IOException ioe) {
			System.out.println("IOException\t" + ioe.getMessage());
		}	catch (Exception e)	{
			System.out.println(e.getMessage());
		}   finally {
			try	{
				if ( null != is )   is.close();
				//if ( null != os )   os.close();
				if ( null != tais ) tais.close();
			}	catch (IOException ioe)	{
			}
		}
	}
	*/

	public static void uncompressZip(final String filePath)	{
		ZipFile zf  =   null;
		try {
			zf  =   new ZipFile(new File(filePath));
			Enumeration<ZipArchiveEntry>    enumZAE =   zf.getEntries();
			while ( enumZAE.hasMoreElements() )	{
				final String    fileName    =   enumZAE.nextElement().getName();
				ZipArchiveEntry	entry	=	zf.getEntry(fileName);
				InputStream	is	=	zf.getInputStream(entry);
				byte[]  bytes    =   getBytes(is, entry.getSize());

				final FileOutputStream	fos	=	new FileOutputStream(fileName);
				fos.write(bytes);
				fos.close();
			}
		}   catch (IOException ioe) {
			System.out.println("IOException\t" + ioe.getMessage());
		}	catch (Exception e)	{
			System.out.println(e.getMessage());
		}	finally	{
			try	{
				if ( null != zf )	zf.close();
			}	catch (IOException ioe)	{
			}
		}
	}
}

