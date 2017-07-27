#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <curl/curl.h>


typedef struct {
	char*   response;
	size_t  size;
} curl_response_t;


static size_t curl_write_function(void* ptr, size_t size, size_t nmemb, curl_response_t* res)
{
	fprintf(stdout, "[curl_write_function] 0\tsize = %zd\tnmemb = %zd\tres->size = %zd\n", size, nmemb, res->size);
	// curl source reference : http://curl.haxx.se/libcurl/c/
	size_t length = res->size + size*nmemb;
	fprintf(stdout, "[curl_write_function] 1\tlength = %zd\n", length);
	res->response = realloc(res->response, length+1);
	if (res->response == NULL) {
		fprintf(stderr, "realloc() failed\n");
		exit(EXIT_FAILURE);
	}
	fprintf(stdout, "[curl_write_function] 2\n");
	memcpy(res->response+res->size, ptr, size*nmemb);
	res->response[length] = '\0';
	res->size = length;
	fprintf(stdout, "[curl_write_function] 3\tres->size = %zd\treturn = %zd\n", res->size, size*nmemb);
	return size*nmemb;
}

curl_response_t* create_curl_response() 
{
	curl_response_t* res = malloc(sizeof(curl_response_t));
	res->size = 0;
	res->response = malloc(res->size+1);
	if ( res->response == NULL ) {
		fprintf(stderr, "malloc() failed\n");
		exit(EXIT_FAILURE);
	}
	res->response[0] = '\0';
	return res;
}

void destroy_curl_response(curl_response_t* res)
{
	fprintf(stdout, "[destroy_curl_response] res->size = %zd\n", res->size);
	if( res ) {
		if( res->response ) free(res->response);
		free(res);
		fprintf(stdout, "[destroy_curl_response]\n");
	}
}

int curl_fetch(curl_response_t* res, char* url, int is_post, char* post_data) 
{
	int				status;
	CURL*			curl;
	CURLcode		res_code;
	int				size;

	fprintf(stdout, "[curl_fetch] url = %s\tis_post = %d\n", url, is_post);
	status = 0;
	curl = curl_easy_init();
	if( curl ) {
		fprintf(stdout, "[curl_fetch] 0\n");
		curl_easy_setopt(curl, CURLOPT_URL, url);
		fprintf(stdout, "[curl_fetch] 1\n");
		curl_easy_setopt(curl, CURLOPT_TIMEOUT, 5L);
		curl_easy_setopt(curl, CURLOPT_LOW_SPEED_TIME, 360L);
		curl_easy_setopt(curl, CURLOPT_NOSIGNAL, 1L);
		//curl_easy_setopt(curl, CURLOPT_TIMEOUT, 1L);
		fprintf(stdout, "[curl_fetch] 2\n");
		if( is_post ) {
			fprintf(stdout, "[curl_fetch][if is_post] 0\n");
			curl_easy_setopt(curl, CURLOPT_POST, 1);
			fprintf(stdout, "[curl_fetch][if is_post] 1\n");
			if( !post_data ) {
				status = 0;
				goto cleanup;
			}
			fprintf(stdout, "[curl_fetch][if is_post] 2\n");
			if( post_data ) {
				size = strlen(post_data);
				fprintf(stdout, "[curl_fetch][if is_post] 3 - 0\tsize = %d\tpost_data = %s\n", size, post_data);
				curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, size);
				curl_easy_setopt(curl, CURLOPT_POSTFIELDS, post_data);
				fprintf(stdout, "[curl_fetch][if is_post] 3 - 1\tsize = %d\tpost_data = %s\n", size, post_data);
			}
			fprintf(stdout, "[curl_fetch][if is_post] 4\n");
		}
		fprintf(stdout, "[curl_fetch] 3\n");
		curl_easy_setopt(curl, CURLOPT_WRITEDATA, res);
		fprintf(stdout, "[curl_fetch] 4 res->size = %zd\tres->response = %s(%zd)\tcurl_write_function = %p\n", res->size, res->response, strlen(res->response), curl_write_function);
		curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, curl_write_function);
		res_code = curl_easy_perform(curl);
		fprintf(stdout, "[curl_fetch] 5 res_code = %d\n", res_code);
		if ( res_code == 0 ) {
		//if ( (res_code = curl_easy_perform(curl)) == 0 ) {
			status = 1;
			fprintf(stdout, "[curl_fetch] curl res = %s\n", res->response);
			goto cleanup;
		}
		fprintf(stdout, "[curl_fetch] 6 curl res = %s\n", res->response);
	}
cleanup :
	curl_easy_cleanup(curl);
	return status;
}

int main()	{
	curl_response_t*	res;
	char				url[140*2];
	int					ret;
	int					is_post;

	res = create_curl_response();
	is_post = 1;
	sprintf(url, "http://www.daum.net/");
	fprintf(stdout, "url = %s\tis_post = %d\n", url, is_post);
	ret = curl_fetch(res, url, is_post, "");
	destroy_curl_response(res);
	return 0;
}
