#include <stdlib.h>
#include <string.h>

#define MIN(x, y)   (x > y ? y : x)

const char STR[] = "Hello World!";
const size_t STR_LEN = 13;

size_t HelloWorld(char* buffer, size_t buffer_length){
  // Copy values from str to buffer and return the number of characters copied
  const size_t N = MIN(STR_LEN, buffer_length);
  memcpy(buffer, STR, N);
  return N;
}
