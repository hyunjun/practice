#include <stdio.h>
#include <sys/time.h>

int main()  {
  int i = 0;
  struct timeval start, end;
  gettimeofday(&start, (void *) 0);
  for ( i = 0; i < 100000000; ++i );
  gettimeofday(&end, (void *) 0);
  float elapsed_time = (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec)/1E6;
  printf("elapsed time = %6.2f sec\n", elapsed_time);
  return 0;
}
