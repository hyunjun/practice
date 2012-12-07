"-----------------------------------------------------------------------"
"	vundle repository
"	git clone git://github.com/gmarik/vundle.git ~/.vim/bundle/vundle	"
"-----------------------------------------------------------------------"
set nocompatible               " be iMproved
filetype off                   " required!

set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

" let Vundle manage Vundle
" required! 
Bundle 'gmarik/vundle'
Bundle 'pyflakes'

" My Bundles here:
"
" original repos on github
"Bundle 'tpope/vim-fugitive'
"Bundle 'Lokaltog/vim-easymotion'
"Bundle 'rstacruz/sparkup', {'rtp': 'vim/'}
"Bundle 'tpope/vim-rails.git'
" vim-scripts repos
"Bundle 'L9'
"Bundle 'FuzzyFinder'
" non github repos
"Bundle 'git://git.wincent.com/command-t.git'

filetype plugin indent on     " required!

set nocompatible               " be iMproved
filetype on
filetype off                   " required!

"
" Brief help
" :BundleList          - list configured bundles
" :BundleInstall(!)    - install(update) bundles
" :BundleSearch(!) foo - search(or refresh cache first) for foo
" :BundleClean(!)      - confirm(or auto-approve) removal of unused bundles
"
" see :h vundle for more details or wiki for FAQ
" NOTE: comments after Bundle command are not allowed..

"	https://github.com/tpope/vim-pathogen
"call pathogen#infect()
"	https://github.com/altercation/vim-colors-solarized
"colorscheme solarized
"-----------------------------------------------------------------------"
"	till here, configurations for Vundle
"-----------------------------------------------------------------------"

if has("gui_running")
	"영문폰트 지정
	set guifont=DejaVu\ Sans\ Mono\ 11
	"한글폰트 지정
	"set guifontwide=Guseul\ 10
	"gVim의 배경테마 설정
	"colorscheme desert
	"gVim 시작시 크기지정
	"set lines=40
	"set co=85
	set background=light
else
	set background=dark
endif
set hls
set ts=4
set shiftwidth=4
"set expandtab
"set autoindent

"	scala syntax highlighting - http://blog.outsider.ne.kr/523
set nu
syntax on
"filetype indent on
"set autoindent
set noic
set hls
set lbr
"colorscheme desert

set textwidth=80
"	if column length goes over 80, change color
"	http://stackoverflow.com/questions/235439/vim-80-column-layout-concerns
highlight OverLength ctermbg=red ctermfg=white guibg=#592929
match OverLength /\%81v.\+/

"au BufWinEnter * if &textwidth > 8
"	\ | let w:m1=matchadd('MatchParen', printf('\%%<%dv.\%%>%dv', &textwidth+1, &textwidth-8), -1)
"	\ | let w:m2=matchadd('ErrorMsg', printf('\%%>%dv.\+', &textwidth), -1)
"	\ | endif

