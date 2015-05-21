#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
  return *(int*)a - *(int*)b;
}

int get_min_diff(int* ar, int n)  {
  int i = 0, min = 10000000;
  for ( i = 0; i < n - 1; ++i ) {
    if ( *(ar + i + 1) - *(ar + i) < min )  {
      min = *(ar + i + 1) - *(ar + i);
    }
  }
  return min;
}

int main()  {
  int n = 0;
  scanf("%d", &n);
  int i = 0;
  int* ar = (int*)malloc(sizeof(int) * n);
  for ( i = 0; i < n; ++i ) {
    scanf("%d", ar + i);
  }

  qsort((void*)ar, n, sizeof(int), compare);

  int min_diff = get_min_diff(ar, n);

  int r_idx = 0;
  int* res = (int*)malloc(sizeof(int) * 2 * (n - 1));
  for ( i = 0; i < n - 1; ++i ) {
    if ( *(ar + i + 1) - *(ar + i) == min_diff )  {
      *(res + r_idx++) = *(ar + i);
      *(res + r_idx++) = *(ar + i + 1);
    }
  }
  printf("%d", *res);
  for ( i = 1; i < r_idx; ++i ) {
    printf(" %d", *(res + i));
  }
  printf("\n");
  free(res);
  free(ar);
  return 0;
}
