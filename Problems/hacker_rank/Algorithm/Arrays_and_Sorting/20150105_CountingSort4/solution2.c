#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STR_LEN 10

int main()  {
  int n = 0, i = 0, idx = 0;
  scanf("%d", &n);

  char** res = (char**) malloc(sizeof(char*) * 100);
  int res_alloc_len = sizeof(char) * n / 2 * MAX_STR_LEN;
  for ( i = 0; i < 100; ++i ) {
    *(res + i) = (char*) malloc(res_alloc_len);
  }

  char tmp[MAX_STR_LEN];
  for ( i = 0; i < n; ++i ) {
    scanf("%d %s", &idx, tmp);
    char* res_tmp = *(res + idx);
    int res_tmp_len = strlen(res_tmp);
    if ( 0 < res_tmp_len )  {
      //strncpy(res_tmp + res_tmp_len, " ", 1);
      *(res_tmp + res_tmp_len) = ' ';
      ++res_tmp_len;
    }
    if ( i < n / 2 )  {
      //strncpy(res_tmp + res_tmp_len, "-", 1);
      *(res_tmp + res_tmp_len) = '-';
    } else  {
      strncpy(res_tmp + res_tmp_len, tmp, strlen(tmp));
    }
  }

  printf("%s", *res);
  for ( i = 1; i < 100; ++i )
    printf(" %s", *(res + i));
  printf("\n");

  for ( i = 0; i < 100; ++i )
    if ( NULL != *(res + i) )
      free(*(res + i));
  if ( NULL != res ) free(res);

  return 0;
}
