#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STR_LEN 11

void counting_sort(int* xs, char** ss, int n)  {
  int i = 0, idx = 0;
  char** res = (char**) malloc(sizeof(char*) * 100);
  for ( i = 0; i < 100; ++i ) {
    *(res + i) = (char*) malloc(sizeof(char) * n * MAX_STR_LEN);
  }
  for ( i = 0; i < n; ++i ) {
    idx = *(xs + i);
    char* tmp = *(res + idx);
    if ( 0 < strlen(tmp) )  {
      strncpy(tmp + strlen(tmp), " ", 1);
    }
    strncpy(tmp + strlen(tmp), *(ss + i), strlen(*(ss + i)));
  }
  printf("%s", *res);
  for ( i = 1; i < 100; ++i )
    if ( 0 < strlen(*(res + i)) )
      printf(" %s", *(res + i));
  printf("\n");
  for ( i = 0; i < n; ++i )
    if ( NULL != *(res + i) )
      free(*(res + i));
  if ( NULL != res )  free(res);
}

int main()  {
  int n = 0, i = 0;
  scanf("%d", &n);
  int* xs = (int*) malloc(sizeof(int) * n);
  char** ss = (char**) malloc(sizeof(char*) * n);
  char tmp[MAX_STR_LEN];
  for ( i = 0; i < n; ++i ) {
    if ( i < n / 2 )  {
      *(ss + i) = (char*) malloc(sizeof(char) * 2);
      strncpy(*(ss + i ), "-", 1);
      scanf("%d %s", xs + i, tmp);
    } else  {
      *(ss + i) = (char*) malloc(sizeof(char) * MAX_STR_LEN);
      scanf("%d %s", xs + i, *(ss + i));
    }
  }
  counting_sort(xs, ss, n);
  for ( i = 0; i < n; ++i )
    if ( NULL != *(ss + i) )
      free(*(ss + i));
  if ( NULL != ss ) free(ss);
  if ( NULL != xs ) free(xs);
  return 0;
}
