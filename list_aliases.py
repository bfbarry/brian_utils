"""
re (lookbacks)
- see my post: https://stackoverflow.com/questions/72209391/regex-to-match-text-after-starting-word-of-a-line
- https://stackoverflow.com/questions/40728902/regex-match-after-word
"""
import re
from os.path import basename, normpath
import sys

# mapping like { sys.argv[1] : <location of rc file> }
RC_LOC = { 'mbp' : '/Users/brianbarry/.zshrc',
           'ucsd': '/home/bfbarry/.bashrc'    }

rc_file = RC_LOC[sys.argv[1]]
with open(rc_file, 'r') as f:
    rc = f.read()

# https://stackoverflow.com/questions/5006716/getting-the-text-that-follows-after-the-regex-match
print(f'Aliases in {basename(normpath(rc_file))}:\n')
[print(a) for a in re.findall(r'^alias (.*)$', rc, re.M) if __file__ not in a] # omit alias for this script
