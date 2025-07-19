# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Path to your Oh My Zsh installation
export ZSH="$HOME/.oh-my-zsh"

# Set Powerlevel10k theme
ZSH_THEME="powerlevel10k/powerlevel10k"

# Oh My Zsh plugins
plugins=(
    git
    sudo
    kubectl
    command-not-found
    zsh-syntax-highlighting
    zsh-autosuggestions
    zsh-completions
    fzf-tab
)

fpath=($HOME/automata-workspace/linq-local-development-platform/scripts/completions $fpath)
# Load Oh My Zsh
source $ZSH/oh-my-zsh.sh

# History configuration
HISTFILE=~/.zsh_history
HISTSIZE=5000
SAVEHIST=5000
setopt share_history
setopt hist_expire_dups_first
setopt hist_ignore_dups
setopt hist_verify
setopt appendhistory
setopt extendedhistory
setopt hist_ignore_space
setopt hist_save_no_dups
setopt hist_find_no_dups

# Completion styling
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color $realpath'
zstyle ':fzf-tab:complete:__zoxide_z:*' fzf-preview 'ls --color $realpath'

# Initialize zoxide
eval "$(zoxide init zsh)"

# Initialize FZF keybindings and completion
# This enables Ctrl+R for history search and Ctrl+T for file search
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
# For homebrew installation
[ -f /opt/homebrew/opt/fzf/shell/key-bindings.zsh ] && source /opt/homebrew/opt/fzf/shell/key-bindings.zsh
[ -f /opt/homebrew/opt/fzf/shell/completion.zsh ] && source /opt/homebrew/opt/fzf/shell/completion.zsh

# Pyenv configuration
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# FZF theme configuration
fg="#CBE0F0"
bg="#011628"
bg_highlight="#143652"
purple="#B388FF"
blue="#06BCE4"
cyan="#2CF9ED"

export FZF_DEFAULT_OPTS="--color=fg:${fg},bg:${bg},hl:${purple},fg+:${fg},bg+:${bg_highlight},hl+:${purple},info:${blue},prompt:${cyan},pointer:${cyan},marker:${cyan},spinner:${cyan},header:${cyan}"

# Use fd instead of fzf default (recursive by default)
export FZF_DEFAULT_COMMAND="fd --type=f --hidden --strip-cwd-prefix --exclude .git"
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
export FZF_ALT_C_COMMAND="fd --type=d --hidden --strip-cwd-prefix --exclude .git"

# Use fd for path completion
_fzf_compgen_path() {
  fd --hidden --exclude .git . "$1"
}

# Use fd for directory completion
_fzf_compgen_dir() {
  fd --type=d --hidden --exclude .git . "$1"
}

# FZF preview configuration
show_file_or_dir_preview="if [ -d {} ]; then eza --tree --color=always {} | head -200; else bat -n --color=always --line-range :500 {}; fi"

export FZF_CTRL_T_OPTS="--preview '$show_file_or_dir_preview'"
export FZF_ALT_C_OPTS="--preview 'eza --tree --color=always {} | head -200'"

# Advanced FZF customization
_fzf_comprun() {
  local command=$1
  shift

  case "$command" in
    cd)           fzf --preview 'eza --tree --color=always {} | head -200' "$@" ;;
    export|unset) fzf --preview "eval 'echo \$'{}"         "$@" ;;
    ssh)          fzf --preview 'dig {}'                   "$@" ;;
    *)            fzf --preview "$show_file_or_dir_preview" "$@" ;;
  esac
}

# Extend PATH
path=(~/bin $path)

# Export environment variables
export GPG_TTY=$TTY

# Source additional local files if they exist
[[ -f ~/.env.zsh ]] && source ~/.env.zsh

# Autoload functions
autoload -Uz zmv

# Define functions and completions
function md() { [[ $# == 1 ]] && mkdir -p -- "$1" && cd -- "$1" }
compdef _directories md

# Git workspace configuration
export GIT_WORKSPACE="~/automata-workspace"
function project {
	local filter="$@"
	local chosen_project=$(git workspace list | fzf -q "$filter")
	if [[ -n $chosen_project ]]; then
		pushd "$GIT_WORKSPACE/$chosen_project"
	fi
}

# Aliases
alias tree='tree -a -I .git'
# Smart cd function: use z for short names, builtin cd for full paths
function cd() {
  if [[ "$1" == /* ]] || [[ "$1" == ~* ]] || [[ "$1" == ".." ]] || [[ "$1" == "." ]] || [[ "$1" == "-" ]]; then
    builtin cd "$@"
  else
    z "$@"
  fi
}
alias ls="eza --icons=always"
alias ll="${aliases[ll]:-ls} -lA"

# Git workspace aliases
alias gws="git workspace status"
alias gwl="git workspace list"
alias cdgw="cd $GIT_WORKSPACE"
alias gwu="git workspace update"

# Git command aliases
alias gco='git checkout'
alias gcm='git commit -m'
alias gaa='git add --all'
alias gam='git add --all && git commit -m'
alias gp='git push'
alias gpl='git pull'
alias gs='git status'
alias gsync='git pull --rebase && git push'
alias gcf='git commit -a --fixup=HEAD'
alias gcfu='git commit --fixup'

# Completion for gcfu to show recent commits with fzf
_gcfu_completion() {
  local commits
  commits=(${(f)"$(git log --pretty=format:'%h %s' --no-merges -n 50)"})
  _describe 'commits' commits
}
compdef _gcfu_completion gcfu

alias devdb='PGPASSWORD=dev psql -h localhost -p 5555 -U dev -d app -c'

# GitHub Copilot
alias gpt='gh copilot suggest'

# Other aliases
alias dc='docker compose'
alias f='fzf'

# Shell options
setopt glob_dots     # no special treatment for file names with a leading dot
setopt no_auto_menu  # require an extra TAB press to open the completion menu

# .NET configuration
export DOTNET_ROOT="$HOME/.dotnet"
export PATH="$DOTNET_ROOT:$PATH"

# opencode
export PATH=/Users/ares/.opencode/bin:$PATH

export LINQ_SERVICE_FRAMEWORK_PUBLISH_FORMAT=json

export OTEL_SDK_DISABLED=true

# coreutils from homebrew
export PATH="/opt/homebrew/opt/coreutils/libexec/gnubin:$PATH"
export PATH="$PATH:$HOME/automata-workspace/linq-local-development-platform/scripts"
export XDG_CONFIG_HOME=$HOME/.config
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
