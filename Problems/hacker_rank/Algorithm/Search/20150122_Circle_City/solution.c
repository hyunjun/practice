#include <stdio.h>
#include <math.h>

int main()  {
  int i = 0, x = 0, t = 0, r = 0, k = 0, cnt = 0;
  scanf("%d", &t);
  for ( i = 0; i < t; ++i ) {
    scanf("%d %d", &r, &k);
    double radius = sqrt(r);
    cnt = 0;
    for ( x = 0; x < radius; ++x )  {
      double dy = sqrt(r - x * x);
      int y = dy;
      if ( y - dy == 0 ) {
        cnt += 4;
      }
    }
    printf("%spossible\n", cnt <= k ? "" : "im");
  }
}
