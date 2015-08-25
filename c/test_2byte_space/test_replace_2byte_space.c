#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>
#include <wchar.h>

void replace_2byte_space(char* dst, const char* src)  {
  int i, idx = 0;
  char* tmp = dst;
  for ( i = 0; i < strlen(src); )  {
    if ( i < strlen(src) - 1 && *(src + i) == 0xffffffC2 && *(src + i + 1) == 0xffffffA0 ) {
      i += 2;
      *(tmp + idx++) = ' ';
      *(tmp + idx++) = ' ';
    } else  {
      *(tmp + idx++) = *(src + i++);
    }
  }
}

void get_whitespace_indices(char* inp, int* starts, int* ends, int* num) {
  int i ;
  *(starts) = 0;
  for ( i = 0; i < strlen(inp); )  {
    if ( isspace(*(inp + i)) )  {
      //printf("[%d] 1byte space\n", i);
      *(ends + *num) = i;
      *(starts + *num + 1) = i + 1;
      ++i;
      ++*num;
    } else if ( i < strlen(inp) - 1 && *(inp + i) == 0xffffffC2 && *(inp + i + 1) == 0xffffffA0 ) {
      //printf("[%d] 2byte space\n", i);
      *(ends + *num) = i;
      *(starts + *num + 1) = i + 2;
      i += 2;
      ++*num;
    } else  {
      //printf("[%d] normal\n", i);
      ++i;
    }
  }
  *(ends + *num) = i;
  ++*num;
}

void str_index_tok(char* buffer, int* starts, int* ends, int num, char** tok) {
  int i;
  for ( i = 0; i < num; ++i ) {
    int l = *(starts + i);
    int r = *(ends + i);
    *(tok + i) = (char*) malloc(sizeof(char) * (r - l + 1));
    memset(*(tok + i), '\0', r - l + 1);
    strncpy(*(tok + i), buffer + l, r - l);
  }
}

int main()  {
  char* buffer = (char*) malloc(sizeof(char) * 1024);

  //wchar_t wsep[] = { 0xC2, 0xA0 };

  while ( fgets(buffer, 1024, stdin) )  {
    printf("------------------- line: %s (strlen %lu)\n", buffer, strlen(buffer));
    //int indices_num = 0;
    //int* start_indices = (int*) malloc(sizeof(int) * strlen(buffer));
    //int* end_indices = (int*) malloc(sizeof(int) * strlen(buffer));
    char* oup = (char*) malloc(sizeof(char) * (strlen(buffer) + 1));
    bzero(oup, strlen(buffer) + 1);
    replace_2byte_space(oup, buffer);

    /*get_whitespace_indices(buffer, start_indices, end_indices, &indices_num);
    //for ( i = 0; i < indices_num; ++i ) {
    //  printf("[%d] %d %d\n", i, *(start_indices + i), *(end_indices + i));
    //}
    char** tok = (char**) malloc(sizeof(char*) * indices_num);
    str_index_tok(buffer, start_indices, end_indices, indices_num, tok);
    free(start_indices);
    free(end_indices);
    printf("count of tokens: %d\n", indices_num);
    for ( i = 0; i < indices_num; ++i ) {
      printf("%s\n", *(tok + i));
      free(*(tok + i));
    }
    free(tok);*/
    printf("converted: %s\n", oup);

    int cnt = 0, start = 0;
    char* org_buffer = strdup(oup);
    char *sep = " \t\r\n";
    char *word = NULL, *brkt = NULL;
    for (word = strtok_r(oup, sep, &brkt); word; word = strtok_r(NULL, sep, &brkt))  {
      //printf("\t[%s]\t%d\t%d\n", word, strstr(org_buffer, word) - org_buffer, strstr(org_buffer, brkt) - org_buffer);
      int end = start + strlen(word);
      char* tmp_word = (char*) malloc(sizeof(char) * (end - start + 1));
      memset(tmp_word, '\0', end - start + 1);
      strncpy(tmp_word, org_buffer + start, end - start);
      printf("\t[%s]\t%d ~ %d\t%s\n", word, start, end, tmp_word);
      start = strstr(org_buffer, brkt) - org_buffer;
      if ( isspace(brkt[0]) )
        ++start;
      free(tmp_word);
      ++cnt;
    }
    printf("\n---------------------\n");
    free(oup);

    /*//if ( cnt <= 1 ) {
      setlocale(LC_CTYPE, "ko_KR.UTF-8");
      wchar_t* wbuffer = (wchar_t*) malloc(sizeof(wchar_t) * (strlen(buffer) + 1));
      memset(wbuffer, '\0', sizeof(wchar_t) * (strlen(buffer) + 1));
      mbstowcs(wbuffer, buffer, strlen(buffer));
      printf("len %d\n", wcslen(wbuffer));

      wchar_t *wword = NULL, *wbrkt = NULL;
      for (wword = wcstok(wbuffer, wsep, &wbrkt); wword; wword = wcstok(NULL, wsep, &wbrkt))  {
        char* tmp = (char*) malloc(sizeof(char) * (wcslen(wword) * 3 + 1));
        memset(tmp, '\0', sizeof(char) * (wcslen(wword) * 3 + 1));
        wcstombs(tmp, wword, wcslen(wword) * 3);
        printf("\t[%s]\t%d\n", tmp, strstr(org_buffer, tmp) - org_buffer);
        free(tmp);
      }
      printf("\n");
    //}
    free(org_buffer);*/
  }

  free(buffer);
  return  0;
}
