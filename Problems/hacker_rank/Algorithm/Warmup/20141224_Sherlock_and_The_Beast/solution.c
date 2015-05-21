#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void decent_number(int N, char** result)  {
  *result = (char*) malloc(sizeof(char) * (N + 1));
  memset(*result, '\0', sizeof(char) * (N + 1));
  int f = 0, t = 0;
  for ( f = N; f >= 0; --f )  {
    if ( f % 3 == 0 ) {
      for ( t = N; t >= 0; --t )  {
        if ( t % 5 == 0 && f + t == N ) {
          memset(*result, '5', f);
          memset(*result + f, '3', t);
          return;
        }
      }
    }
  }
  *(*result + 0) = '-';
  *(*result + 1) = '1';
  *(*result + 2) = '\0';
}

int main()  {
  int T = 0;
  scanf("%d", &T);
  while ( T-- ) {
    int N = 0;
    scanf("%d", &N);
    char* res;
    decent_number(N, &res);
    if ( res != NULL )  {
      printf("%s\n", res);
      free(res);
    }
  }
  return 0;
}
