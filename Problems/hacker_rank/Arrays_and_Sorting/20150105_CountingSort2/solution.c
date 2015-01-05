#include <stdio.h>
#include <stdlib.h>

void counting_sort(int* ar, int n)  {
  int* counts = (int*) malloc(sizeof(int) * n);
  int i = 0;
  for ( i = 0; i < n; ++i ) {
    ++*(counts + *(ar + i));
  }
  int idx = 0;
  int* res = (int*) malloc(sizeof(int) * n);
  for ( i = 0; i < n; ++i ) {
    int c = *(counts + i);
    while ( c-- )  {
      *(res + idx++) = i;
    }
  }
  printf("%d", *res);
  for ( i = 1; i < n; ++i ) {
    printf(" %d", *(res + i));
  }
  printf("\n");
  free(res);
}

int main()  {
  int n = 0;
  scanf("%d", &n);
  int i = 0;
  int* ar = (int*) malloc(sizeof(int) * n);
  for ( i = 0; i < n; ++i ) {
    scanf("%d", ar + i);
  }
  counting_sort(ar, n);
  free(ar);
  return 0;
}
