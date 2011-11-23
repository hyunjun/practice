package com.knoa.practice;

import	org.apache.commons.cli.CommandLine;
import	org.apache.commons.cli.CommandLineParser;
import	org.apache.commons.cli.HelpFormatter;
import	org.apache.commons.cli.Option;
import	org.apache.commons.cli.OptionBuilder;
import	org.apache.commons.cli.Options;
import	org.apache.commons.cli.ParseException;
import	org.apache.commons.cli.PosixParser;

/**
 *	http://commons.apache.org/cli/usage.html
 */
public class App 
{
    public static void main( String[] args ) throws Exception
    {
		/*
		Options	options	=	new Options();

		options.addOption("t", false, "display current time");
		options.addOption("c", true, "country code");

		CommandLineParser	parser	=	new PosixParser();
		CommandLine	cmd	=	parser.parse(options, args);

		if ( cmd.hasOption("t") )	{
			System.out.println("option t exists");
		}	else	{
			System.out.println("option t does NOT exist");
		}
		if ( cmd.hasOption("c") )	{
			String	countryCode	=	cmd.getOptionValue("c");
			System.out.print("country code:\t");
			if ( null == countryCode )
				System.out.print("use default");
			else
				System.out.print(countryCode);
			System.out.println();
		}	else	{
			System.out.println("country code does NOT exist");
		}
		*/

		//	http://commons.apache.org/cli/usage.html
		//	create the command line parser
		CommandLineParser	parser	=	new PosixParser();

		//	create the Options
		Options	options	=	new Options();
		Option	option	=	new Option("a", "all", false, "do not hide entries starting with .");
		option.setRequired(true);
		options.addOption(option);
		options.addOption("A", "almost-all", false, "do not list implied .  and ..");
		options.addOption("b", "escape", false, "print octal escapes for nongraphic " +
			"characters");
		options.addOption(OptionBuilder.withLongOpt("block-size")
			.withDescription("use SIZE-byte blocks")
			.hasArg()
			.withArgName("SIZE")
			.isRequired()
			.create()
			);
		options.addOption("B", "ignore-backups", false, "do not list implied entried " +
			"ending with ~");
		options.addOption("c", false, "with -lt: sort by, and show, ctime (time of last " +
			"modification of file status information) with " +
			"-l:show ctime and sort by name otherwise: sort " +
			"by ctime");
		options.addOption("C", false, "list entries by columns");

		HelpFormatter	formatter	=	new HelpFormatter();
		//String[]	arguments	=	new String[]{ "--block-size=10" };

		try	{
			//	parse the command line arguments
			CommandLine	line	=	parser.parse(options, args);

			//	validate that block-size has been set
			if ( line.hasOption("block-size") )	{
				//	print the value of block-size
				System.out.println(line.getOptionValue("block-size"));
			}
		}	catch (ParseException exp)	{
			formatter.printHelp("apache-commons-cli", options);
			System.out.println( "\nUnexpected exception:" + exp.getMessage());
		}
    }
}
