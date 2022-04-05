:set number
:set nowrap
:set autoindent
:set tabstop=4
:set shiftwidth=4
:set smarttab
:set softtabstop=4

call plug#begin()

Plug 'https://github.com/tpope/vim-surround' " surrounding ysw )
Plug 'https://github.com/tpope/vim-commentary' "for commenting gcc & gc
Plug 'https://github.com/ap/vim-css-color' "css color preview
Plug 'https://github.com/rafi/awesome-vim-colorschemes' " retro scheme
Plug 'https://github.com/ryanoasis/vim-devicons' " developer icons
Plug 'https://github.com/tc50cal/vim-terminal' " vim terminal
Plug 'https://github.com/vim-airline/vim-airline'
Plug 'https://github.com/preservim/nerdtree' " NerdTree
Plug 'https://github.com/preservim/tagbar' " tagbar for code navigation
Plug 'https://github.com/neoclide/coc.nvim' " auto completion
Plug 'https://github.com/jiangmiao/autopairs'

call plug#end()

nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTee<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-i> :PlugInstall<CR>
nnoremap <C-b> :TagbarToggle<CR>
nnoremap <C-s> :w<CR>
nnoremap <C-q> :q!<CR>

inoremap <expr> <Tab> pumvisible() ? coc#_select_confirm() : "<Tab>"
