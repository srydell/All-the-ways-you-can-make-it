# All the ways you can :make it #

A small summary of a talk I held at [Stockholm Vim meetup at Devies May 24 2019](https://www.meetup.com/Stockholm-Vim-Meetup/events/261201356/).

## Running your program from vim ##

### Via a terminal ###

There is nothing wrong with the terminal - so use it! From normal mode you can type `:!` to make everything thereafter be sent to the underlying shell. For running a python program you could define a neat shortcut as

```vim
:nnoremap <leader>r :!python3 <C-R>%<CR>
```

so that whenever you press `<leader>r` (by default `<leader>` is `\`) vim will send `python3 current_file.py` to the underlying shell (assuming you have the file `current_file.py` in your open buffer).

If you use `tmux`, you might like the [vimux plugin](https://github.com/benmills/vimux) that will allow you to send commands from one vim instance to a separate `tmux` pane. This avoids having to wait for the shell command to finish before continuing to edit your file. You also don't have to suspend your current vim instance and drop down to the shell.

### How to :make it ###

`:make` is a command specifically for building and running programs from within vim. Whenever the command is invoked, the `makeprg` variable is checked and then ran as if it were a shell command. By default the `makeprg` is simply `make` (check it by typing `:echo &makeprg` from normal mode). Which is a bit C-centric, but we can of course change it. Keeping with our `python` example

```vim
:set makeprg=python3\ %
```

creates a command with equivalent behaviour to the example from before. Only now, you don't have to temporarily suspend your vim instance and the output is piped into the [`quickfix`](http://vimdoc.sourceforge.net/htmldoc/quickfix.html#quickfix) list. This is a real hint, since what is in the `quickfix` is usually parsed and tagged text. So how do we parse the output from `:make`? Vim provides a structured way of doing this through the `errorformat` variable. It has a whole mountain of options that I won't bore you with (you can check it by typing `:echo &errorformat` from normal mode). As per usual with things that are difficult and tedious, someone else has probably done it - enter `:compiler`, a command that sets `makeprg` and `errorformat`. The one we want is called `pyunit` from an old unit test framework (fortunately for us, the output from `python` hasn't changed much). Set it by typing
```vim
:compiler pyunit
```

This does not however populate `makeprg` since there are multiple ways of running a `python` program.

Now you'll see that all errors get caught in a nicely formatted `quickfix` list that you can navigate between errors with `:cnext` and `:cprevious`.

### Dispatch the saviour ###

While `:make` is great it is still fully synchronous, meaning that your vim instance will freeze until whatever command is in `makeprg` has finished running.

This is solved with [vim-dispatch](https://github.com/tpope/vim-dispatch) from the famous [tpope](https://github.com/tpope). It adds the `:Make` command which runs `makeprg` in a whole separate process, freeing your vim instance to do whatever.

So now we can run whichever `python` script is in our current buffer. But what about when the file is a unit test, or perhaps always need some special parameters? Tpope also built a plugin called [vim-projectionist](https://github.com/tpope/vim-projectionist) that allows us to define meta data where we can store a file specific `makeprg`. The meta data is stored in the file `.projections.json` typically located in your project root directory.

With a project structure as

```
.
├── shark
│   ├── __init__.py
│   └── shark.py
└── test
    ├── __init__.py
    └── test_shark.py
```

We might have the meta data in `.projections.json` as

```json
{
    "shark/*.py": {
        "make": "python3 shark/{}.py"
    },
    "test/test_*.py": {
        "make": "python3 -m unittest test.test_{}"
    }
}
```

So that whenever we are working on a unit test, the `makeprg` is set to run our test suite. This allows you to create very complex structures where everything is just the way you want it.

There is of course not one correct way to run or build a program from vim, I use all of the methods described here. But by exploring multiple of them allows you to choose the best tool for your job and perhaps even forgetting the rest. Remember to [sharpen the saw](https://moolenaar.net/habits.html).

---

# Further reading #

* [`:help quickfix`](http://vimdoc.sourceforge.net/htmldoc/quickfix.html#quickfix)
* [`:help errorformat`](http://vimdoc.sourceforge.net/htmldoc/quickfix.html#errorformat)
* [`:help :compiler`](http://vimdoc.sourceforge.net/htmldoc/quickfix.html#:compiler)
* [vimux plugin](https://github.com/benmills/vimux) - Plugin to interact with tmux panes from vim
* [vim-dispatch](https://github.com/tpope/vim-dispatch) - Plugin to asynchronously build and test programs
* [vim-projectionist](https://github.com/tpope/vim-projectionist) - Plugin to add meta data to your project
