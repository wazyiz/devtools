syntax on

set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nu
set relativenumber
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch

set colorcolumn=80
set signcolumn=yes
highlight ColorColumn ctermbg=0 guibg=lightgrey

call plug#begin('~/.vim/plugged')

"Plug 'nvim-telescope/telescope.nvim'
Plug 'gruvbox-community/gruvbox'
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
Plug 'mg979/vim-visual-multi', { 'branch': 'master' }
Plug 'tpope/vim-commentary' "for commenting gcc & gc
Plug 'jiangmiao/auto-pairs'
Plug 'prettier/vim-prettier', {'do': 'yarn install --frozen-lockfile --production'}
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tpope/vim-fugitive'
Plug 'vim-airline/vim-airline'
Plug 'junegunn/fzf', {'do': {-> fzf#install()}}
Plug 'junegunn/fzf.vim'

call plug#end()

let mapleader = ' '
let g:deoplete#enable_at_startup = 1
colorscheme gruvbox

" mappings
" open explorer
nnoremap <C-t> :Ex<CR>
" write file
nnoremap <leader>s :w<CR>
" close file
nnoremap <leader>q :q<CR>
" format file
nnoremap <leader>p :Prettier<CR>
" open FZF
nnoremap <leader>f :Files<CR>
" open Git files with FZF
nnoremap <leader>gf :GFiles<CR>
" open Bufffers, type buffer number then enter
nnoremap <leader>b :Buffers<CR>
" open terminal :below terminal
nnoremap <leader>bt :bel term<CR>

" remap ESC
imap jj <Esc>
