#include <stdio.h>
#include <stdlib.h>

void counting_sort(int* ar, int n)  {
  int* counts = (int*) malloc(sizeof(int) * 100);
  int i = 0;
  for ( i = 0; i < n; ++i ) {
    ++*(counts + *(ar + i));
  }
  for ( i = 1; i < 100; ++i ) {
    if ( 0 < *(counts + i) )  {
      *(counts + i) += *(counts + i - 1);
    } else if ( 0 == *(counts + i) )  {
      *(counts + i) = *(counts + i - 1);
    }
  }
  printf("%d", *counts);
  for ( i = 1; i < 100; ++i ) {
    printf(" %d", *(counts + i));
  }
  printf("\n");
  free(counts);
}

int main()  {
  int n = 0;
  scanf("%d", &n);
  int i = 0;
  int* ar = (int*) malloc(sizeof(int) * n);
  char tmp[1024];
  for ( i = 0; i < n; ++i ) {
    scanf("%d %s", ar + i, tmp);
  }
  counting_sort(ar, n);
  free(ar);
  return 0;
}
