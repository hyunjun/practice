#include <stdio.h>
#include <stdlib.h>

void partition(int* ar, int n, int** res)  {
  int pivot = *ar;
  int i = 0, idx = 0;
  for ( i = 0; i < n; ++i ) {
    if ( *(ar + i) < pivot )  {
      *(*res + idx++) = *(ar + i);
    }
  }
  *(*res + idx++) = pivot;
  for ( i = 0; i < n; ++i ) {
    if ( pivot < *(ar + i) )  {
      *(*res + idx++) = *(ar + i);
    }
  }
}

int main()  {
  int n = 0;
  scanf("%d", &n);
  int* ar = (int*) malloc(sizeof(int) * n);
  int* res = (int*) malloc(sizeof(int) * n);
  int i = 0;
  for ( i = 0; i < n; ++i ) {
    scanf("%d", ar + i);
  }
  partition(ar, n, &res);

  printf("%d", *res);
  for ( i = 1; i < n; ++i )
    printf(" %d", *(res + i));
  printf("\n");

  free(ar);
  free(res);
  return 0;
}
