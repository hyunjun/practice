#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX_STR_LEN 1000

int is_pangram(char* s) {
  int dict[26] = {0,};
  int i = 0;
  for ( i = 0; i < strlen(s); ++i )
    ++dict[tolower(*(s + i)) - 'a'];
  for ( i = 0; i < 26; ++i )
    if ( dict[i] == 0 )
      return 0;
  return 1;
}

int main(void)  {
  char s[MAX_STR_LEN] = {'\0',};
  fgets(s, MAX_STR_LEN, stdin);
  if ( 0 == is_pangram(s) )
    printf("not ");
  printf("pangram\n");
  return 0;
}
