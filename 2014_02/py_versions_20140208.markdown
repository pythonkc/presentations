!SLIDE

## Managing Python Versions
###(in OS X, UNIX, and GNU/Linux)

!SLIDE left

1. Install [Homebrew](http://brew.sh/) (OS X only)
    * If you're not familiar with the command line, be sure to read the [documentation](https://github.com/Homebrew/homebrew/wiki)
2. Install [bash](http://www.gnu.org/software/bash/) (version 4.0 or greater)
    * OS X
        1. `$ brew install bash`
        2. `$ sudo echo "/usr/local/bin/bash" >> /private/etc/shells"`
        3. `$ chsh -s /usr/local/bin/bash {username}`
        4. Close and reopen your terminal program
    * Other systems, use your package manager to install bash 4.0 (or greater)
3. Install [Python 3](http://docs.python.org/3/)
    * OS X: `$ brew install python3`
    * Other systems, use your package manager to install Python 3
4. Install [Python 2](http://docs.python.org/2/)
    * OS X: `$ brew install python`
    * Other systems, use your package manager to install Python 2
