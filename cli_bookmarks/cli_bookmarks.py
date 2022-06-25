import subprocess as sp
import json
import argparse
import os


BOOKMARK_PATH = os.path.dirname(__file__) + '/bookmarks.json'
SHELL_PATH = sp.check_output('echo $SHELL', shell=True).decode("utf-8").replace('\n','') # for zsh get weird source .zshrc error
    

try:
    with open(BOOKMARK_PATH, 'r') as f:
        bookmarks = json.load(f) # {"bookmark": "path/to/cd"}
except FileNotFoundError:
    bookmarks = {}


def save_bookmark(bookmark, path):
    """
    shell call: python cli_bookmarks.py -s {bookmark} {path}
    use path = `pwd` to save current path
    """
    if bookmarks.get(bookmark):
        print('Bookmark already exists!\n')
        return
    bookmarks[bookmark] = path
    with open(BOOKMARK_PATH, 'w') as f:
        json.dump(bookmarks, f, indent=4)


def print_bookmarks():
    """shell call: python cli_bookmarks.py -p"""
    print(json.dumps(bookmarks, indent=4))


def goto_bookmark(bookmark):
    """shell call: python cli_bookmarks.py -g {bookmark}"""
    if not bookmarks.get(bookmark):
        print('bookmark does not exist!')
        return
    print(bookmarks[bookmark])
    

def del_bookmark(bookmark):
    """shell call: python cli_bookmarks.py -d"""
    if not bookmarks.get(bookmark):
        print('bookmark does not exist!\n')
        return
    print(f'Deleting bookmark {bookmark} -> {bookmarks[bookmark]}')
    del bookmarks[bookmark]
    with open(BOOKMARK_PATH, 'w') as f:
        json.dump(bookmarks, f)


def init(rc_path):
    """
    concat to bashrc 
    shell call: python cli_bookmarks.py -d (only run once or if __file__ path changes)
    """
    cmd = f'python3 {__file__}'
    config = [ '\n\n# >>> cli_bookmarks init >>>\n',
               f'function s() {{ echo $({cmd} -s $1 $2); }}\n', # need echoes in case of print() to not pass as command
               f'function g() {{ cd "$({cmd} -g $1)"; }}\n',
               f'function p() {{ echo $({cmd} -p); }}\n',
               f'function d() {{ echo $({cmd} -d $1); }}\n',
               '# <<< cli_bookmarks init <<<' ]
    with open(rc_path, 'r') as f:
        rc = f.readlines()
    
    all_text = ''.join(rc)
    if cmd in all_text: # same state; do nothing
        print('already initialized')
    
    elif 'cli_bookmarks.py' in all_text: # different path
        i1, i2 = rc.index(config[0]), rc.index(config[-1]) + 1
        rc = rc[:i1] + rc[i2:] + config # remove existing config
        with open(rc_path, 'w') as f:
            f.writelines(rc)
        sp.call(f'source {rc_path}', shell=True, executable=SHELL_PATH)
        print(f'changed cmd path to {__file__}')
        
    else:
        rc += config
        with open(rc_path, 'w') as f:
            f.writelines(rc)
        sp.call(f'source {rc_path}', shell=True, executable=SHELL_PATH)
        print(f'initialized config with cmd path at {__file__}')


if __name__ == '__main__':
    # take in cli arg input
    # call one of the functions with that input
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='save', nargs=2)
    parser.add_argument('-g', dest='go')
    parser.add_argument('-p', dest='print', action='store_true')
    parser.add_argument('-d', dest='delete')
    parser.add_argument('-i', dest='init')

    args = parser.parse_args()
    # print('right here!', args, flush=True)
    if args.save:
        save_bookmark(args.save[0], args.save[1])
    elif args.go:
        goto_bookmark(args.go)
    elif args.print:
        print_bookmarks()
    elif args.delete:
        del_bookmark(args.delete)
    elif args.init:
        init(args.init)