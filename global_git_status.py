"""
Check status of all git repos from START_DIR
"""

import os
from os.path import isdir, join
import subprocess as sp
import pandas as pd


# this version is slower
def OLDdive_and_status(path):
    """
    recursively look for git status
    stop under two conditions: if .git in dir, or if no other dirs in dir
    """
    status_dict = {'repo':[], 'committed':[]}
    def recurse(path):
        if sum([isdir(join(path, f)) for f in os.listdir(path)]) == 0:
            # print('halted at sum')
            return
        for f in os.listdir(path):
            if f == '.git':
                os.chdir(path)
                git_status = sp.check_output('git status', shell=True).decode('utf-8')
                if 'Changes not staged' in git_status or 'Untracked files' in git_status:
                    status = 0
                else:
                    status = 1
                status_dict['repo'].append(path.replace(START_DIR+'/', ''))
                status_dict['committed'].append(status)
                return
            elif isdir(join(path, f)):
                recurse(join(path, f))
    recurse(path)
    return status_dict


def dive_and_status(path):
    status_dict = {'repo':[], 'committed':[]}
    for f in os.walk(path):
        curr_path, ls = f[0], f[1]
        if len(ls) > 0: # a directory with content
            if '.git' in ls:
                os.chdir(curr_path)
                git_status = sp.check_output('git status', shell=True).decode('utf-8')
                if 'Changes not staged' in git_status or 'Untracked files' in git_status:
                    status = 0
                else:
                    status = 1
                status_dict['repo'].append(curr_path.replace(START_DIR+'/', ''))
                status_dict['committed'].append(status)
    return status_dict


START_DIR = '/Users/brianbarry/Desktop' # abs path


if __name__ == '__main__':
    import time
    start = time.time()
    status_dict = dive_and_status(START_DIR)
    print(pd.DataFrame(status_dict).to_string(index=False))
    print(f'\nTook {time.time() - start:.2f} seconds')