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
"Plug 'vim-visual-multi', { 'branch': 'master' }
Plug 'jiangmiao/auto-pairs'

call plug#end()

let g:deoplete#enable_at_startup = 1
colorscheme gruvbox

" remaps
nnoremap <C-s> :w!<CR>
nnoremap <C-q> :q!<CR>
