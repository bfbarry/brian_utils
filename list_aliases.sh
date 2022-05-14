#!/bin/bash

# get location of rc file from arg
if [ "$1" = "mbp" ]
    then
    RC_FILE="/Users/brianbarry/.zshrc"
elif [ "$1" = "ucsd" ]
    then
    RC_FILE="/home/bfbarry/.bashrc"
fi

echo "Aliases in `basename $RC_FILE`:\n"
# to omit last line : https://stackoverflow.com/questions/4881930/remove-the-last-line-from-a-file-in-bash
# to replace word   : https://stackoverflow.com/questions/13570327/how-to-delete-a-substring-using-shell-script
cat $RC_FILE | grep ^alias | tail -r | tail -n +2 | tail -r | sed 's/\alias //g'


# old code to check map machine to rc location with a "dict"
# needs Bash4: https://stackoverflow.com/questions/1494178/how-to-define-hash-tables-in-bash
# w/ Bash3, super hacky "dictionary" :
# RC_LOC=( "mbp:/Users/brianbarry/.zshrc"
#          "ucsd:/home/bfbarry/.bashrc" )
#
# for m in "${RC_LOC[@]}" ; do
#     if [ "$1" = "${m%%:*}" ]
#     then
#         RC_FILE="${m##*:}"
#     fi
# done