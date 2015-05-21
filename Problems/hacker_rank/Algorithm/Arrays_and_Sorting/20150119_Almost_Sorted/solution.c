#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void* b) {
  return *(int*)a - *(int*)b;
}

int has_same_contents(int* ar1, int* ar2, int n)  {
  int i = 0;
  for ( i = 0; i < n; ++i )
    if ( *(ar1 + i) != *(ar2 + i) )
      return 0;
  return 1;
}

void swap(int* ar, int l, int r)  {
  int tmp = *(ar + l);
  *(ar + l) = *(ar + r);
  *(ar + r) = tmp;
}

void is_possible_to_sort(int* ar, int n)  {
  int l = 0, r = n - 1, i = 0;
  while ( l < r && *(ar + l) < *(ar + l + 1) )  ++l;
  while ( 0 < r && *(ar + r - 1) < *(ar + r) )  --r;

  int* sorted = (int*)malloc(sizeof(int) * n);
  memcpy(sorted, ar, sizeof(int) * n);
  qsort((void*)sorted, n, sizeof(int), compare);

  swap(ar, l, r);
  if ( has_same_contents(sorted, ar, n) )  {
    printf("yes\nswap %d %d\n", l + 1, r + 1);
    free(sorted);
    return;
  }
  int l_tmp = l + 1;
  int r_tmp = r - 1;
  while ( l_tmp < r_tmp ) swap(ar, l_tmp++, r_tmp--);
  if ( has_same_contents(sorted, ar, n) )  {
    printf("yes\nreverse %d %d\n", l + 1, r + 1);
  } else  {
    printf("no\n");
  }
  free(sorted);
}

int main()  {
  int n = 0, i = 0;
  scanf("%d", &n);
  int* ar = (int*)malloc(sizeof(int) * n);
  for ( i = 0; i < n; ++i ) {
    scanf("%d", ar + i);
  }
  is_possible_to_sort(ar, n);
  free(ar);
}
