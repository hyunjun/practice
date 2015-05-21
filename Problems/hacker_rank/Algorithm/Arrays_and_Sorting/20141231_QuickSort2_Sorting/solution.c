#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print(int* ar, int n)  {
  int i = 0;
  printf("%d", *ar);
  for ( i = 1; i < n; ++i )
    printf(" %d", *(ar + i));
  printf("\n");
}

void quick_sort(int* ar, int n, int** res)  {
  int pivot = *ar;
  int i = 0, idx = 0;
  int l_size = 0;
  for ( i = 0; i < n; ++i ) {
    if ( *(ar + i) < pivot )  {
      ++l_size;
    }
  }
  int* left = NULL;
  int* l_res = NULL;
  if ( 0 < l_size ) {
    left = (int*) malloc(sizeof(int) * l_size);
    l_res = (int*) malloc(sizeof(int) * l_size);
    idx = 0;
    for ( i = 0; i < n; ++i ) {
      if ( *(ar + i) < pivot )  {
        *(left + idx++) = *(ar + i);
      }
    }
    if ( 1 < l_size ) {
      quick_sort(left, l_size, &l_res);
      print(l_res, l_size);
    } else  {
      *l_res = *left;
    }
  }
  int r_size = 0;
  for ( i = 0; i < n; ++i ) {
    if ( pivot < *(ar + i) )  {
      ++r_size;
    }
  }
  int* right = NULL;
  int* r_res = NULL;
  if ( 0 < r_size ) {
    right = (int*) malloc(sizeof(int) * r_size);
    r_res = (int*) malloc(sizeof(int) * r_size);
    idx = 0;
    for ( i = 0; i < n; ++i ) {
      if ( pivot < *(ar + i) )  {
        *(right + idx++) = *(ar + i);
      }
    }
    if ( 1 < r_size ) {
      quick_sort(right, r_size, &r_res);
      print(r_res, r_size);
    } else  {
      *r_res = *right;
    }
  }
  idx = 0;
  if ( l_res != NULL ) {
    /*for ( i = 0; i < l_size; ++i ) {
      *(*res + idx++) = *(l_res + i);
    }*/
    memcpy(*res + idx, l_res, sizeof(int) * l_size);
    idx += l_size;
    free(left);
    free(l_res);
  }
  *(*res + idx++) = pivot;
  if ( r_res != NULL )  {
    /*for ( i = 0; i < r_size; ++i ) {
      *(*res + idx++) = *(r_res + i);
    }*/
    memcpy(*res + idx, r_res, sizeof(int) * r_size);
    //idx += r_size;
    free(right);
    free(r_res);
  }
}

int main()  {
  int n = 0;
  scanf("%d", &n);
  int* ar = (int*) malloc(sizeof(int) * n);
  int* res = (int*) malloc(sizeof(int) * n);
  int i = 0;
  for ( i = 0; i < n; ++i ) {
    scanf("%d", ar + i);
  }
  quick_sort(ar, n, &res);

  print(res, n);

  free(ar);
  free(res);
  return 0;
}
