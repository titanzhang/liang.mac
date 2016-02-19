set nocompatible
 
call pathogen#infect()
call pathogen#helptags()
 
filetype plugin on
filetype indent on
 
" encoding
set encoding=utf8
set ffs=unix,dos,mac
 
" files
set nobackup
set nowb
set noswapfile

" syntax highlight color
syntax on

" color scheme
color ron

" 4 spaces as tab
set tabstop=2
set softtabstop=2
set shiftwidth=2
set expandtab
set smarttab

" indent
set autoindent
set smartindent
set wrap

" line number
set nu
map <C-N><C-N> :set nu!<CR>
