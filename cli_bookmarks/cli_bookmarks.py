import subprocess as sp
import json
import argparse

from regex import W


with open('bookmarks.json', 'w') as f:
    bookmarks = json.load(f) # {"bookmark": "path/to/cd"}


def save_bookmark(bookmark, path):
    """
    shell call: python cli_bookmarks.py -s {bookmark} {path}
    use path = `pwd` to save current path
    """
    bookmarks[bookmark] = path
    with open('bookmarks.json', 'w') as f:
        json.dump(bookmarks, f)


def print_bookmarks():
    """shell call: python cli_bookmarks.py -p"""
    print(bookmarks)


def goto_bookmark(bookmark):
    """shell call: python cli_bookmarks.py -g {bookmark}"""
    print(bookmarks[bookmark])
    

def del_bookmark(bookmark):
    """shell call: python cli_bookmarks.py -d"""
    del bookmarks[bookmark]
    with open('bookmarks.json', 'w') as f:
        json.dump(bookmarks, f)


def init(rc_path):
    """
    concat to bashrc 
    shell call: python cli_bookmarks.py -d (only run once or if __file__ path changes)
    """
    cmd = f'python3 {__file__}'
    config = [ "# >>> cli_bookmarks init >>>",
               f"alias s='{cmd} -s $1 $2'",
               f"function g() {{cd $({cmd} -g $1) }}'",
               f"alias p='{cmd} -p'",
               f"alias d='{cmd} -d $1'",
               "# <<< cli_bookmarks init <<<" ]
    with open(rc_path, 'r') as f:
        rc = f.readlines()
    
    all_text = ''.join(rc)
    if cmd in all_text: # same state; do nothing
        print('already initialized')
    
    elif 'cli_bookmarks.py' in all_text: # different path
        i1, i2 = rc.index(config[0]), rc.index(config[-1]) + 1
        rc = rc[:i1] + rc[i2:] + config # remove existing config
        with open(rc_path, 'w') as f:
            f.write('\n'.join(rc))
        sp.call(f'source {rc_path}')
        print(f'changed cmd path to {cmd}')
        
    else:
        rc += config
        print(f'initialized config with cmd path at {cmd}')


if __name__ == 'main':
    # take in cli arg input
    # call one of the functions with that input
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='save', nargs=2)
    parser.add_argument('-g', dest='go')
    parser.add_argument('-p', dest='print', action='store_true')
    parser.add_argument('-d', dest='delete')
    parser.add_argument('-i', dest='init')

    args = parser.parse_args()

    if args.save:
        save_bookmark(args.save[0], args.save[1])
    elif args.go:
        goto_bookmark(args.go[0])
    elif args.print:
        print_bookmarks()
    elif args.delete:
        del_bookmark(args.delete)
    elif args.init:
        init(args.init)