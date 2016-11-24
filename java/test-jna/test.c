#include <stdio.h>
#include <string.h>

void exampleMethod(const char* value) {
  printf("%s\n", value);
}

int example_of_add_strlen(const char* s1, const char* s2)  {
  int l1 = 0;
  int l2 = 0;
  if ( s1 != NULL ) {
    l1 = strlen(s1);
  }
  if ( s2 != NULL ) {
    l2 = strlen(s2);
  }
  return l1 + l2;
}

int example_of_int(int a, int b)  {
  return a + b;
}

float example_of_float(float a, float b)  {
  return a + b;
}
