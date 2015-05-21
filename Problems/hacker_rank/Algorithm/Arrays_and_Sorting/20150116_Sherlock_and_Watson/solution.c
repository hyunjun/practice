#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()  {
  int i = 0, N = 0, K = 0, Q = 0;
  scanf("%d %d %d", &N, &K, &Q);
  int* ar = (int*)malloc(sizeof(int) * N);
  for ( int i = 0; i < N; ++i ) {
    scanf("%d", ar + i);
  }
  K %= N;
  int* tmp = (int*)malloc(sizeof(int) * K);
  int idx = N - K;
  memcpy(tmp, ar + idx, sizeof(int) * K);
  memcpy(ar + N - idx, ar, sizeof(int) * (N - K));
  memcpy(ar, tmp, sizeof(int) * K);
  for ( int i = 0; i < Q; ++i ) {
    int q = 0;
    scanf("%d", &q);
    printf("%d\n", *(ar + q));
  }
  free(tmp);
  free(ar);
  return 0;
}
