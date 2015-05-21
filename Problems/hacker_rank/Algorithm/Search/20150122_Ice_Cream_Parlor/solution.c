#include <stdio.h>
#include <stdlib.h>

void flavor_index(int* ar, int n, int m)  {
  int i = 0, j = 0;
  for ( i = 0; i < n - 1; ++i ) {
    for ( j = i + 1; j < n; ++j ) {
      if ( *(ar + i) + *(ar + j) == m ) {
        printf("%d %d\n", i + 1, j + 1);
        return;
      }
    }
  }
}

int main()  {
  int t = 0, m = 0, n = 0, i = 0, j = 0;
  int* ar = NULL;
  scanf("%d", &t);
  for ( i = 0; i < t; ++i ) {
    scanf("%d", &m);
    scanf("%d", &n);
    ar = (int*)malloc(sizeof(int) * n);
    for ( j = 0; j < n; ++j ) {
      scanf("%d", ar + j);
    }
    flavor_index(ar, n, m);
    free(ar);
  }
  return 0;
}
