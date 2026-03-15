# To-do list in terminal (Command Line Interface)

A simple, fast command-line todo list manager — stored locally in `~/.todo.json`.

---
## Installation

Paste this into your terminal:

```bash
curl -sSL https://raw.githubusercontent.com/ArtashesSoghomonyan/todo-list-cli/main/scripts/install.sh | bash
```

That's it. The installer will:

- Check for Python 3.12+
- Download the source to `~/.local/share/todo-list-cli`
- Create an isolated virtual environment and install dependencies
- Place a `todo` command in `~/.local/bin`
- Add `~/.local/bin` to your `$PATH` if it isn't already there

After installation, open a new terminal (or run `source ~/.bashrc` || `source ~/.zshrc`) and you're ready to go.

---
## Requirements

- Python 3.12 or newer
- `git` or `curl`/`wget` (for downloading the source)
- Linux or macOS (Windows is not supported by the installer yet)

---
## Usage

```
todo --help
```

| Command | Short | Description |
|---|---|---|
| `todo --list` | `todo -l` | Show all todos |
| `todo --add "Task name"` | `todo -a "Task name"` | Add a new todo |
| `todo --check N` | `todo -c N` | Mark todo #N as done ✅ |
| `todo --uncheck N` | `todo -u N` | Mark todo #N as undone ⬜ |
| `todo --remove N` | `todo -r N` | Remove todo #N from the list |

### Examples

```bash
# Add some todos
todo --add "Buy groceries"
todo --add "Read a book"
todo --add "Call the dentist"

# List all todos
todo --list
1. ⬜ Buy groceries
2. ⬜ Read a book
3. ⬜ Call the dentist

# Mark the first one as done
todo --check 1

# List again
todo --list
1. ✅ Buy groceries
2. ⬜ Read a book
3. ⬜ Call the dentist

# Remove a todo
todo --remove 2

# Uncheck a completed todo
todo --uncheck 1
```

---
## Data storage

Your todos are saved locally at:

```
~/.todo.json
```

The file is plain JSON, so you can inspect or back it up at any time:

```bash
cat ~/.todo.json
```

---
## Uninstallation

```bash
curl -sSL https://raw.githubusercontent.com/ArtashesSoghomonyan/todo-list-cli/main/scripts/uninstall.sh | bash
```

You will be asked whether you also want to delete your todo data (`~/.todo.json`).
