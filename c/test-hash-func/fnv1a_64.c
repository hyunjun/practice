//  https://github.com/twitter/twemproxy/blob/master/src/hashkit/nc_fnv.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUFFER_SIZE 1024

static uint64_t FNV_64_INIT = UINT64_C(0xcbf29ce484222325);
static uint64_t FNV_64_PRIME = UINT64_C(0x100000001b3);

uint32_t
hash_fnv1a_64(const char *key, size_t key_length)
{
  uint32_t hash = (uint32_t) FNV_64_INIT;
  size_t x;

  for (x = 0; x < key_length; x++) {
    uint32_t val = (uint32_t)key[x];
    hash ^= val;
    hash *= (uint32_t) FNV_64_PRIME;
  }

  return hash;
}

int main()  {
  char buffer[MAX_BUFFER_SIZE];
  while (fgets(buffer, MAX_BUFFER_SIZE, stdin) != NULL) {
    //  https://stackoverflow.com/questions/2693776/removing-trailing-newline-character-from-fgets-input
    buffer[strcspn(buffer, "\n")] = 0;
    uint32_t hashed_val = hash_fnv1a_64(buffer, 24);
    printf("%s\t%u\t%d\n", buffer, hashed_val, hashed_val % 10);
    bzero(buffer, MAX_BUFFER_SIZE);
  }
  return 0;
}
