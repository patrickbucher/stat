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

## Magic Commands

- `%paste`: paste code from the clipboard
- `%cpaste`: paste multiple code snippets interactively, end with `--`
- `%run`: run a script and keep the loaded symbols in the REPL
- `%history`: display the command history
    - `%history -n 1-4`: display from the first to the fourth command
- `%rerun`: run a part of the history again
- `%save`: store the history in a file
- `%lsmagic`: list magic functions
- `%xmode`: set exception reporting mode
    - `Plain`: most compact, least information
    - `Context`: more information
    - `Verbose`: most detailed output
- `%load_ext`: load the extension with the given name
- `%%file`/`%%writefile`: write the following code section to a file with the given file name
    `-a` for appending instead of overwriting

To get help on a magic command, use the question mark notation as with any
other command. Example: `%rerun?` shows the documentation for the `%rerun`
magic command.

- `%automagic`: toggle automagic setting

If `%automagic` is set, shell commands like `cat`, `cp`, `env`, `ls`, `man`,
`mkdir`, `more`, `mv`, `pwd`, `rm`, `rmdir` can be used without prefixes.
Otherwise, a `%` prefix is needed.

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

## Shell Interaction

- `!` at the beginning of a line: execute a shell command
- `files = !ls -l`: store output of a shell command as a list
    - `files.grep('foo')`: filter list by `'foo'`
    - `files.fields(1, 2)`: display columns 1 and 2 of the output
- `!mkdir {folder}`: create a directory with the variable `folder`'s value as a name
    - surround a Python variable with curly braces to make it available for the shell

## Miscellaneous

- `;` at the end of a line: suppress output

## Debugging

Python's standard debugger is `pdb`. IPython comes with an enhanced version `ipdb`.

- `%debug`: start a debugging session starting from the last exception
- `%pdb on`: start debugging session automatically when an exception occurs

Debugging sessions have special commands (usually, only the first letters needs to be typed):

- `l(ist)`: show the current location in the file
- `u(p)`/`d(own)`: move up and down in the call stack
- `n(ext)`: execute current line and move to next line (step over)
- `s(tep)`: enter the function (step in)
- `r(eturn)`: leave the function (step out)
- `q(uit)`: leave the debugging session and exit the program execution
- `c(ontinue)`: leave the debugging session, but keep the program running
- `<Enter>`: repeat previous command
- `p(rint)`: print variables
- `h(help)`: display a list of all available commands or help to the command argument supplied

## Timing and Profiling

### Timing

- `%time`: measure the execution time of a single statement/function call
    - The garbage collector will be deactivated so that the result is not biased.
- `%timeit`: measure the average execution time of a single statement/function call after repeated runs
    - The number of runs will be determined automatically.
- `%%timeit`: as above, but working on whole sections of code

### Runtime Profiling

- `%prun`: runtime profile of a single statement/function call using Python's built-in profiler
- `%lprun`: line by line runtime profile of a single statement/function call
    - install with `pip install line_profiler` on the shell
    - load with `%load_ext line_profiler` in IPython

### Memory Profiling

- install with `pip install memory_profiler` on the shell
- load with `%load_ext memory_profiler` in IPython
- `%memit`: memory profile of a single statement/function call
- `%mprun`: line by line memory profile of a single function call

`%mprun` requires the profiled code to be in it's own module. Example session:

    %load_ext memory_profiler
    %%file fibonacci.py
    def fib(n):
        if n == 1 or n == 2:
            return 1
        return fib(n-1) + fib(n-2)

    from fibonacci import fib
    %mprun -f fib fib(35)

