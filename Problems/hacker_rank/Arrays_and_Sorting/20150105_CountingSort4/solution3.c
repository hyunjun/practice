#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STR_LEN 11

int main()  {
  int n = 0, i = 0, idx = 0;
  scanf("%d", &n);

  int res_str_len = n / 2 * MAX_STR_LEN;
  char* res[100];
  for ( i = 0; i < 100; ++i ) {
    //memset(res[i], '\0', res_str_len);
    //res[i] = (char*) malloc(res_str_len);
    res[i] = NULL;
  }

  char tmp[MAX_STR_LEN];
  for ( i = 0; i < n; ++i ) {
    scanf("%d %s", &idx, tmp);
    char* res_tmp = res[idx];
    if ( NULL == res_tmp )  {
      res[idx] = (char*) malloc(res_str_len);
      res_tmp = res[idx];
    }
    int res_tmp_len = strlen(res_tmp);
    if ( 0 < res_tmp_len )  {
      strncpy(res_tmp + res_tmp_len, " ", 1);
      //res_tmp[res_tmp_len] = ' ';
      ++res_tmp_len;
    }
    if ( i < n / 2 )  {
      strncpy(res_tmp + res_tmp_len, "-", 1);
      //res_tmp[res_tmp_len] = '-';
    } else  {
      strncpy(res_tmp + res_tmp_len, tmp, strlen(tmp));
    }
  }

  if ( NULL != res[0] )
    printf("%s", res[0]);
  for ( i = 1; i < 100; ++i )
    if ( NULL != res[i] )
      printf(" %s", res[i]);
  printf("\n");

  for ( i = 0; i < 100; ++i ) {
    free(res[i]);
  }

  return 0;
}
