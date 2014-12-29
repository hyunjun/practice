#include <stdio.h>
#include <stdlib.h>

void insertion_sort(int* arr, int s)  {
  int i = 0, j = 0;
  for ( i = 1; i < s; ++i ) {
    for ( j = i; j > 0; --j ) {
      if ( *(arr + j) < *(arr + j - 1) )  {
        int tmp = *(arr + j);
        *(arr + j) = *(arr + j - 1);
        *(arr + j - 1) = tmp;
      }
    }
  }
  printf("%d", *arr);
  for ( j = 1; j < s; ++j ) {
    printf(" %d", *(arr + j));
  }
  printf("\n");
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
