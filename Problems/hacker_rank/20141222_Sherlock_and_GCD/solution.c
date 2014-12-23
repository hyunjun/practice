#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NUM 100001

int has_subset(int* arr, int arr_size)  {
  int i = 0;
  int max_num = 0;
  for ( i = 0 ; i < arr_size; ++i ) {
    if ( max_num < *(arr + i) ) {
      max_num = *(arr + i);
    }
  }

  int set[MAX_NUM];
  int prime[MAX_NUM];
  memset(prime, '\0', sizeof(int) * MAX_NUM);
  int check = 2, prime_index = 0;
  while ( check < max_num + 1 ) {
    int is_prime_number = 1;
    for ( i = 0; i < prime_index; ++i ) {
      if ( prime[i] < check && check % prime[i] == 0 )  {
        is_prime_number = 0;
        break;
      }
    }
    if ( 0 == is_prime_number ) {
      ++check;
      continue;
    }
    memset(set, '\0', sizeof(int) * MAX_NUM);
    for ( i = 0; i < arr_size; ++i )  {
      ++set[*(arr + i) % check];
    }
    int is_empty_set = 1;
    for ( i = 1; i < MAX_NUM; ++i )  {
      if ( 0 < set[i] ) {
        is_empty_set = 0;
        break;
      }
    }
    if ( 1 == is_empty_set )
      return 0;
    prime[prime_index++] = check;
    ++check;
  }
  return 1;
}

int main()  {
  int T = 0;
  fscanf(stdin, "%d", &T);
  int i = 0, j = 0, N = 0;
  for ( i = 0; i < T; ++i ) {
    fscanf(stdin, "%d", &N);
    int* arr = (int*) malloc(sizeof(int) * N);
    for ( j = 0; j < N; ++j ) {
      fscanf(stdin, "%d", arr + j);
    }
    if ( 1 == has_subset(arr, N) )
      printf("YES\n");
    else
      printf("NO\n");
    free(arr);
  }
  return 0;
}
