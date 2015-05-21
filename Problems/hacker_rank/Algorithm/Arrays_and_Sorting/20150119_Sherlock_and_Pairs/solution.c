#include <stdio.h>
#include <stdlib.h>

#define MAX_CNT 1000000

long num_of_pairs(int* ar, int n)  {
  int i = 0;
  long cnt = 0;
  int cnt_array[MAX_CNT] = {0, };
  for ( int i = 0; i < n; ++i ) {
    ++cnt_array[*(ar + i) - 1];
  }
  for ( int i = 0; i < MAX_CNT; ++i ) {
    if ( 1 < cnt_array[i] ) {
      cnt += ((long) cnt_array[i]) * (cnt_array[i] - 1);
    }
  }
  return cnt;
}

int main()  {
  int T = 0, i = 0, j = 0;
  scanf("%d", &T);
  for ( i = 0; i < T; ++i ) {
    int n = 0;
    scanf("%d", &n);
    int* ar = (int*)malloc(sizeof(int) * n);
    for ( j = 0; j < n; ++j ) {
      scanf("%d", ar + j);
    }
    printf("%ld\n", num_of_pairs(ar, n));
    free(ar);
  }
  return 0;
}
