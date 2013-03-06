#!/bin/bash

if [[ $# = 0 ]]; then
    echo "Turning ON show-all-files"
    defaults write com.apple.finder AppleShowAllFiles -boolean yes
    exit 0
fi

if [[ $1 = off ]]; then
    echo "Turning OFF show-all-files"
    defaults write com.apple.finder AppleShowAllFiles -boolean no
else
    echo -e \
    "\tUsage: $0\t# turns on show all files\n\
    \tUsage: $0 off\t# turns off show all files\n\
    \tAnd relaunch Finder in both cases for switch to take place"
fi


