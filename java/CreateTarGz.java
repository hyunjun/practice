import	java.io.*;

import	org.apache.commons.compress.archivers.tar.TarArchiveEntry;
import	org.apache.commons.compress.archivers.tar.TarArchiveOutputStream;
import	org.apache.commons.compress.compressors.gzip.GzipCompressorOutputStream;
import	org.apache.commons.compress.utils.IOUtils;

//	http://www.thoughtspark.org/node/53
/*
<dependency>
	<groupId>org.apache.commons</groupId>
	<artifactId>commons-compress</artifactId>
	<version>1.2</version>
</dependency>

javac -cp ~/.m2/repository/org/apache/commons/commons-compress/1.2/commons-compress-1.2.jar ./CreateTarGz.java
java -cp ~/.m2/repository/org/apache/commons/commons-compress/1.2/commons-compress-1.2.jar:. CreateTarGz [dir to compress] [.tar.gz filepath]
 */
public class CreateTarGz	{
	public static void createTarGzOfDirectory(String directoryPath, String tarGzPath)
		throws IOException {

		FileOutputStream fOut = null;
		BufferedOutputStream bOut = null;
		GzipCompressorOutputStream gzOut = null;
		TarArchiveOutputStream tOut = null;

		try {
			fOut = new FileOutputStream(new File(tarGzPath));
			bOut = new BufferedOutputStream(fOut);
			gzOut = new GzipCompressorOutputStream(bOut);
			tOut = new TarArchiveOutputStream(gzOut);

			addFileToTarGz(tOut, directoryPath, "");
		} finally {
			tOut.finish();

			tOut.close();
			gzOut.close();
			bOut.close();
			fOut.close();
		}
	}

	private static void addFileToTarGz(TarArchiveOutputStream tOut, String path, String base)
		throws IOException {

		File f = new File(path);
		String entryName = base + f.getName();
		TarArchiveEntry tarEntry = new TarArchiveEntry(f, entryName);

		tOut.setLongFileMode(TarArchiveOutputStream.LONGFILE_GNU);
		tOut.putArchiveEntry(tarEntry);

		if (f.isFile()) {
			IOUtils.copy(new FileInputStream(f), tOut);

			tOut.closeArchiveEntry();
		} else {
			tOut.closeArchiveEntry();

			File[] children = f.listFiles();

			if (children != null) {
				for (File child : children) {
					addFileToTarGz(tOut, child.getAbsolutePath(), entryName + "/");
				}
			}
		}
	}

	public static void main( String[] args ) throws IOException {
		CreateTarGz.createTarGzOfDirectory(args[0], args[1]);
	}
}
