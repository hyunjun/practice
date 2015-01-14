#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long merge(int* arr, int l, int r)  {
  if ( r - l < 2 )  {
    return 0;
  }
  int i = 0;
  int m = (r + l) / 2;
  long l_cnt = merge(arr, l, m);
  long r_cnt = merge(arr, m, r);
  long cnt = l_cnt + r_cnt;
  int* tmp = (int*)malloc(sizeof(int) * (r - l));
  memset(tmp, '\0', sizeof(int) * (r - l));
  int l_idx = l, r_idx = m, t_idx = 0;
  while ( l_idx < m && r_idx < r )  {
    if ( *(arr + l_idx) <= *(arr + r_idx) ) {
      *(tmp + t_idx++) = *(arr + l_idx++);
    } else  {
      cnt += m - l_idx;
      *(tmp + t_idx++) = *(arr + r_idx++);
    }
  }
  while ( l_idx < m ) *(tmp + t_idx++) = *(arr + l_idx++);
  while ( r_idx < r ) *(tmp + t_idx++) = *(arr + r_idx++);
  //memcpy(arr + l, tmp, sizeof(int) * t_idx);
  for ( i = l; i < l + t_idx; ++i ) *(arr + i) = *(tmp + i - l);
  free(tmp);
  return cnt;
}

void merge_sort(int* arr, int n, long* ret)  {
  *ret = merge(arr, 0, n);
}

int main()  {
  int t = 0, i = 0, n = 0, j = 0;
  long ret = 0;
  scanf("%d", &t);
  for ( i = 0; i < t; ++i ) {
    scanf("%d", &n);
    int* arr = (int*) malloc(sizeof(int) * n);
    for ( j = 0; j < n; ++j ) {
      scanf("%d", arr + j);
    }
    merge_sort(arr, n, &ret);
    printf("%ld\n", ret);
    free(arr);
  }
  return 0;
}
