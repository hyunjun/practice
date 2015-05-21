#include <stdio.h>
#include <stdlib.h>

int main()  {
  int V = 0, n = 0, i = 0;
  scanf("%d", &V);
  scanf("%d", &n);
  int* arr = (int*) malloc(sizeof(int) * n);
  for ( i = 0; i < n; ++i ) {
    scanf("%d", arr + i);
  }
  for ( i = 0; i < n; ++i ) {
    if ( *(arr + i) == V )  {
      printf("%d\n", i);
    }
  }
  free(arr);
  return 0;
}
