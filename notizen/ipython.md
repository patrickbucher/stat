# IPython

## Help

- `help([symbol])` or `[symbol]?`: display the docstring of the symbol
    - Example: `help(map)` or `map?`
- `[symbol]??`: display the source code of the symbol (only if written in
  Python)
- `<Tab>`-completion: display matching `dir()` entries
- `*` (wildcard): matches any (also empty) string

## Readline Commands

- `C` means `Ctrl`
- `M` means `Alt`

### Navigation

- `C-a`: move to beginning of the line
- `C-e`: move to end of the line
- `C-f`: move one character forward
- `C-b`: move one character backward
- `A-f`: move one word forward
- `A-b`: move one word backward

### Manipulation

- `C-d`: delete character under the cursor
- `A-d`: delete rest of the word under the cursor (right side)
- `C-k`: delete to the end of the line (right side)
- `C-u`: delete the beginning of the line (left side)
- `C-y`: yank (paste) text deleted before
- `C-t`: transpose; move character under the cursor one position to the left

### History

- `C-p`: previous command (type multiple times to move back through the
  history)
- `C-n`: next command (type multiple times to move forth through the history)
- `C-r`:  search backward in history

### Miscellaneous

- `C-l`: clear screen
- `C-c`: cancel current command
- `C-d`: terminate session

## Magic Commands

- `%paste`: paste code from the clipboard
- `%cpaste`: paste multiple code snippets interactively, end with `--`
- `%run`: run a script and keep the loaded symbols in the REPL
- `%timeit`: benchmark the execution time of a single command
- `%%timeit`: benchmark the execution time of a multi-line code section
- `%history`: display the command history
    - `%history -n 1-4`: display from the first to the fourth command
- `%rerun`: run a part of the history again
- `%save`: store the history in a file
- `%lsmagic`: list magic functions

To get help on a magic command, use the question mark notation as with any
other command. Example: `%rerun?` shows the documentation for the `%rerun`
magic command.

## History

Lines of input and output are numbered so that single lines can be addressed:

- `In`: list of all inputs
    - `In[4]`: fourth input line
- `Out`: map of all outputs
    - `Out[2]`: second output line
- `_` (single underscore): last output
- `__` (double underscore): second to the last output
- `___` (triple underscore): third to the last output
- `_n` (single underscore with number): n to the last output `_4` = `Out[4]`

## Miscellaneous

- `!` at the beginning of a line: execute a shell command
- `;` at the end of a line: suppress output
