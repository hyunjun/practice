#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
  return *(int*)a - *(int*)b;
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

  printf("%d\n", *(ar + n / 2));
  free(ar);
  return 0;
}
