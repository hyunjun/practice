#include <stdio.h>
#include <stdlib.h>

void counting_sort(int* ar, int n)  {
  int* res = (int*) malloc(sizeof(int) * 100);
  int i = 0;
  for ( i = 0; i < n; ++i ) {
    ++*(res + *(ar + i));
  }
  printf("%d", *res);
  for ( i = 1; i < 100; ++i ) {
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
