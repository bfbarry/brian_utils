#!/bin/bash
usage()
{
echo "Usage: sh `basename $0` color 'text'"
exit 1
}

if [ $# -ne 2 ] ; then
    usage
fi

echo "<span style=\"color:$1\">$2</span>"
