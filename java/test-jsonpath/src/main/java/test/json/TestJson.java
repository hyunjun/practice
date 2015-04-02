package test.json;

import org.apache.commons.io.IOUtils;

import java.io.*;
import java.util.*;
import java.net.URI;
import java.net.URL;
import java.net.URLConnection;
import java.net.HttpURLConnection;

import org.codehaus.jackson.JsonFactory;
import org.codehaus.jackson.JsonGenerationException;
import org.codehaus.jackson.JsonParseException;
import org.codehaus.jackson.JsonParser;
import org.codehaus.jackson.JsonToken;
import org.codehaus.jackson.map.JsonMappingException;
import org.codehaus.jackson.map.ObjectMapper;
import org.codehaus.jackson.type.TypeReference;
//import org.codehaus.jackson.annotate.JsonIgnoreProperties;

import com.alibaba.fastjson.*;

class Blog      {
	private String request;
	private float load;
	private long min_sid;
	private long max_sid;
	private String used_time;
	private List<String> next_urls;
	private String log_message;
	private int exception_count;
	private String format_version;
	private List<Exceptions> exceptions;

	public List<String> getNextUrls()       {       return next_urls;       }
	public void setNextUrls(List<String> _next_urls)        {       next_urls = _next_urls; }
	public List<Exceptions> getExceptions()     {       return exceptions;    }
	public void setExceptions(List<Exceptions> _exceptions)   {       exceptions = _exceptions;   }
}
class Exceptions      {
	private String sid;
	private String type;
	private Map<String, Object> exception;
	private Map<String, String> source;
}

public class TestJson	{
	private static ObjectMapper	mapper = new ObjectMapper(); // can reuse, share globally
	static	{
		mapper.configure(JsonParser.Feature.ALLOW_UNQUOTED_FIELD_NAMES, true);
		//mapper.configure(DeserializationConfig.Feature.FAIL_ON_UNKNOWN_PROPERTIES, false);
	}

	public static void dump(String urlStr, String jsonString)	throws Exception	{
		Map<String, Object> jsonResult = null;
		List<String> nextUrls = null;
		Map<String, Object> docMap = null;
		URL url = null;
		for ( int i = 0; i < 1; ++i )	{
			try	{
				url = new URL(urlStr);
				jsonResult = mapper.readValue(url, new TypeReference<Map<String, Object>>() { });
				//jsonResult = mapper.readValue(jsonString, new TypeReference<Map<String, Object>>() { });

				nextUrls = (List<String>) jsonResult.get("next_urls");
				if ( null == nextUrls || nextUrls.size() <= 0 )	{ break; }

				for ( final Map<String, Object> dataMap : ((List<Map<String, Object>>) jsonResult.get("data")) )	{
					docMap = ((Map<String, Object>) dataMap.get("document"));
					String.format("%s\t%s\t%s\t%s\n", dataMap.get("doc_id"),docMap.get("title"),docMap.get("description"),docMap.get("posturl"));
				}
			}	catch (JsonMappingException e)	{
				e.printStackTrace();
			}	catch (JsonGenerationException e)	{
				e.printStackTrace();
			}	catch (JsonParseException e)	{
				e.printStackTrace();
			}	catch (IOException e)	{
				//e.printStackTrace();
				URLConnection urlConn = url.openConnection();
				System.out.println(urlConn.toString());
				HttpURLConnection httpUrlConn = (HttpURLConnection) urlConn;
				System.out.println(httpUrlConn.toString());
				//System.out.println("IOEXCEPTION\t" + new Scanner(httpUrlConn.getInputStream(), "UTF-8").useDelimiter("\\A").next());
				System.out.println("IOEXCEPTION\t" + httpUrlConn.getRequestMethod());
				//System.out.println("IOEXCEPTION\t" + httpUrlConn.getResponseMessage());
			}
		}
	}

	public static void dump2(String jsonString)	throws Exception	{
		List<String> nextUrls = null;
		Map<String, Object> docMap = null;
		for ( int i = 0; i < 1; ++i )	{
			try	{
				JSONObject jsonResult = JSON.parseObject(jsonString);

				nextUrls = (List<String>) jsonResult.get("next_urls");
				if ( null == nextUrls || nextUrls.size() <= 0 )	{ break; }

				for ( final Map<String, Object> dataMap : ((List<Map<String, Object>>) jsonResult.get("data")) )	{
					docMap = ((Map<String, Object>) dataMap.get("document"));
					String.format("%s\t%s\t%s\t%s\n", dataMap.get("doc_id"),docMap.get("title"),docMap.get("description"),docMap.get("posturl"));
				}
			}	catch (Exception e)	{
			}
		}
	}
    public static void main( String[] args ) throws Exception
    {
		//final String url = "http://10.25.34.15:8080/convbridge/v2/nlpblogdump/r1/static/10.33.127.29/3/documents?count=1000&to_table=3&from=100000002&to=149999997&";
		final String url = "http://10.25.34.18:8080/convbridge/v2/nlpblogdump/r1/static/10.33.127.87/5/documents?to=749999996&count=1000&to_table=5&from=740651547&";
		System.out.println("IOUtils " + IOUtils.readLines(new URL(url).openStream(), "UTF-8").get(0));
		//String jsonString = new Scanner(new URL(url).openStream(), "UTF-8").useDelimiter("\\A").next();
		String jsonString = null;
		long start, end, durationJ, durationF, sumJ = 0, sumF = 0;

		int cnt = 1;
		for ( int i = 0; i < cnt; ++i )	{
			start = System.currentTimeMillis();
			dump(url, jsonString);
			end = System.currentTimeMillis();
			durationJ = (end - start);
			System.out.printf("%d", durationJ);
			sumJ += durationJ;

			/*start = System.currentTimeMillis();
			dump2(jsonString);
			end = System.currentTimeMillis();
			durationF = (end - start);
			System.out.printf("\t%d", durationF);
			sumF += durationF;*/

			System.out.println();
		}
		System.out.printf("sum\t%d\t%d\navg\t%f\t%f\n", sumJ, sumF, sumJ * 1. / cnt, sumF * 1. / cnt);
    }
}
