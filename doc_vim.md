# _vimrc
```
set ts=2
set shiftwidth=2
if has("gui_running")
  set guifont=Consolas:h11
  "  Korean
  "set guifontwide=Guseul\ 10
  colorscheme darkblue
  set hls!
  set wrap
  "set lines=40
  "set co=85
endif
```
  * http://stackoverflow.com/questions/3316244/set-gvim-font-in-vimrc-file
  * gvim portable; GVimPortable\App\DefaultData\settings\vimrc
* etc
  * replace시 개행 문자 입력
    * ^M (Ctrl+V, Ctrl+M)
    * http://mwultong.blogspot.com/2007/08/vim-vi-m-m.html
  * syntax highlighting이 되지 않는 경우
    * 보통 기본 vi나 vim-minimal만 설치된 경우 발생
    * vim-enhanced 설치
* links
  * http://shinlucky.tistory.com/117
  * http://happyoutlet.tistory.com/11
  * http://www.ibm.com/developerworks/kr/library/tutorial/l-vi/index.html
  * vim dictionary; http://hisjournal.net/blog/242
