package net.daum;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class App	{
	private static Logger logger = LogManager.getLogger();

    public static void main( String[] args )	{
        System.out.println( "Hello World!" );
		logger.debug("Debug message");
		logger.info("Info message");
		logger.warn("Warn message");
		logger.error("Error message");
		logger.fatal("Fatal message");
    }
}
