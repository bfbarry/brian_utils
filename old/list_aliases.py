"""
can't figure proper way to do with re (lookbacks)
- see my post: https://stackoverflow.com/questions/72209391/regex-to-match-text-after-starting-word-of-a-line
- https://stackoverflow.com/questions/40728902/regex-match-after-word

just using a shell script for this now
"""
import re
from os.path import basename, normpath
import sys

# mapping like { sys.argv[1] : <location of rc file> }
RC_LOC = { 'mbp' : '/Users/brianbarry/.zshrc',
           'ucsd': '/home/bfbarry/.bashrc'    }

RC_FILE = RC_LOC[sys.argv[1]]
with open(RC_FILE, 'r') as f:
    rc = f.read()

# pat = re.compile('^alias') # https://stackoverflow.com/questions/5006716/getting-the-text-that-follows-after-the-regex-match
print(f'Aliases in {basename(normpath(RC_FILE))}:\n')
# [print(a) for a in re.findall(pat, rc)[1:-1]] # omit first comment and alias for this script

## Using loop instead
# for l in rc.split('\n'):
#     try:
#         if l.split()[0] == 'alias':
#             print(l.replace('alias ', ''))
#     except:
#         continue
    