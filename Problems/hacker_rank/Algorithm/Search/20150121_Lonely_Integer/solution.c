#include <stdio.h>

int main()  {
  int n = 0, i = 0, tmp = 0;
  scanf("%d", &n);
  int ar[101] = { 0, };
  for ( i = 0; i < n; ++i ) {
    scanf("%d", &tmp);
    ++ar[tmp - 1];
  }
  for ( i = 0; i <= 101; ++i )  {
    if ( 1 == ar[i] ) {
      printf("%d\n", i + 1);
      break;
    }
  }
  return 0;
}
