#!/usr/bin/env bash

# Configuration
REPO_URL="https://github.com/ArtashesSoghomonyan/todo-list-cli"
INSTALL_DIR="${HOME}/.local/share/todo-list-cli"
BIN_DIR="${HOME}/.local/bin"
COMMAND_NAME="todo"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

info() {
    echo -e "${BLUE}[info] $* ${NC}"
}

success() {
    echo -e "${GREEN}[ok] $* ${NC}"
}

warn() {
    echo -e "${YELLOW}[warn] $* ${NC}"
}

error() {
    echo -e "${RED}[error] $* ${NC}" >&2; exit 1
}

# Confirm prompt
confirm() {
    local prompt="$1"
    local answer=""
    read -r -p "$(echo -e "${YELLOW}[?]${NC}     ${prompt} [y/N] ")" answer
    case "$answer" in
        [yY][eE][sS]|[yY]) return 0 ;;
        *) return 1 ;;
    esac
}

# Remove launcher
remove_launcher() {
    local launcher="${BIN_DIR}/${COMMAND_NAME}"

    if [ -f "$launcher" ]; then
        rm -f "$launcher"
        success "Removed launcher: ${launcher}"
    else
        warn "Launcher not found at ${launcher} — skipping."
    fi
}

# Remove installation directory
remove_install_dir() {
    if [ -d "$INSTALL_DIR" ]; then
        rm -rf "$INSTALL_DIR"
        success "Removed installation directory: ${INSTALL_DIR}"
    else
        warn "Installation directory not found at ${INSTALL_DIR} — skipping."
    fi
}

# Optionally remove todo data
remove_data() {
    local data_file="${HOME}/.todo.json"

    if [ -f "$data_file" ]; then
        echo ""
        info "Your todo data file was found at ${data_file}."
        if confirm "Do you also want to delete your todo data?"; then
            rm -f "$data_file"
            success "Removed todo data: ${data_file}"
        else
            info "Todo data kept at ${data_file}."
        fi
    fi
}

# Remove PATH entry from shell rc
clean_path_entry() {
    local shell_rc=""
    case "${SHELL:-}" in
        */zsh)  shell_rc="${HOME}/.zshrc" ;;
        */bash) shell_rc="${HOME}/.bashrc" ;;
        */fish) shell_rc="${HOME}/.config/fish/config.fish" ;;
        *)      shell_rc="${HOME}/.profile" ;;
    esac

    if [ -f "$shell_rc" ] && grep -q "Added by todo-list-cli installer" "$shell_rc"; then
        # Remove the comment line and the path line that follow it
        sed -i '/# Added by todo-list-cli installer/{N;d;}' "$shell_rc"
        # Also remove any blank line directly before the comment if one remains
        success "Removed PATH entry from ${shell_rc}."
    fi
}

# Main
main() {
    echo ""
    echo -e "${BOLD}  Uninstalling todo-list-cli${NC}"
    echo    "  ────────────────────────────"
    echo ""

    # Bail out early if nothing is installed
    if [ ! -f "${BIN_DIR}/${COMMAND_NAME}" ] && [ ! -d "$INSTALL_DIR" ]; then
        warn "todo-list-cli does not appear to be installed. Nothing to do."
        echo ""
        exit 0
    fi

    if ! confirm "Are you sure you want to uninstall todo-list-cli?"; then
        info "Uninstall cancelled."
        echo ""
        exit 0
    else
        echo ""
        remove_launcher
        remove_install_dir
        clean_path_entry
        remove_data

        echo ""
        echo -e "${GREEN}${BOLD}  todo-list-cli has been uninstalled.${NC}"
        echo ""
    fi
}

main "$@"
