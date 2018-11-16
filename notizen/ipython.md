# IPython

## Help

- `help([symbol])` or `[symbol]?`: display the docstring of the symbol
    - Example: `help(map)` or `map?`
- `[symbol]??`: display the source code of the symbol (only if written in Python)
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

- `C-p`: previous command (type multiple times to move back through the history)
- `C-n`: next command (type multiple times to move forth through the history)
- `C-r`:  search backward in history

### Miscellaneous

- `C-l`: clear screen
- `C-c`: cancel current command
- `C-d`: terminate session
