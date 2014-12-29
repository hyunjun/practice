#include <stdio.h>
#include <stdlib.h>

void print_arr(int* arr, int s) {
  int i = 0;
  printf("%d", *arr);
  for ( i = 1; i < s; ++i ) {
    printf(" %d", *(arr + i));
  }
  printf("\n");
}

void insertion_sort(int* arr, int s)  {
  int V = *(arr + s - 1);
  int idx = s - 2;
  while ( -1 < idx && V < *(arr + idx) )  {
    *(arr + idx + 1) = *(arr + idx);
    print_arr(arr, s);
    --idx;
  }
  *(arr + idx + 1) = V;
  print_arr(arr, s);
}

int main()  {
  int s = 0;
  scanf("%d", &s);
  int* arr = (int*) malloc(sizeof(int) * s);
  int i = 0;
  for ( i = 0; i < s; ++i ) {
    scanf("%d", arr + i);
  }
  insertion_sort(arr, s);
  free(arr);
  return 0;
}
