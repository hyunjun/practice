tokenization of 1, 2 byte space mixed string
============================================
* problem; 1, 2 byte space가 혼용된 문자열을 whitespace character로 tokenization을 하며, 각 token의 시작, 끝 index가 필요
  * 1 byte space; 0x20, 0x09, 0x0D, 0x0A
  * 2 byte space; 0xC2 & 0xA0
  * 1 byte space만 있으면, isspace로 찾을 수 있으며, fgets(char*,...)로 읽어 strtok_r로 tokenization 가능
  * 2 byte space만 있으면, iswspace로 찾을 수 있으며, (setlocale 설정 필요) fgetws(wchar_t*,...)로 읽어 wcstok로 tokenization 가능
  * 하지만 혼용된 문자열의 경우는 위와 같이 처리할 수 없음
* solution
  * `replace_2byte_space` string을 읽으며 그대로 복사를 하되, 2 byte space의 경우는 1 byte space로 둘 다 치환
  * `start + strlen(word)`를 사용해 현재 token의 끝 index를 계산
  * `strstr(org_buffer, brkt) - org_buffer`를 사용해 다음 token의 시작 index를 계산
    * `if ( isspace(brkt[0]) ) ++start` 단 2 byte space가 있는 경우 token의 첫 번째 byte가 space이므로, 시작 index를 하나 증가
