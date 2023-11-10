import os


def am_i_on_wsl():
    try:
        return 'microsoft' in os.uname().release.lower()
    except AttributeError:
        return False
    

def c_path(path):
    """
    formats paths on the C drive to work on WSL or Windows
    path (str):  must be windows like path e.g., /Users/...
    """
    if '/mnt/c' not in path and am_i_on_wsl():
        path_part = path[1:] if path[0] == '/' or path[0] == '\\' else path # for os.path.join to work
        path = os.path.join('/mnt/c', path_part)
    return path
