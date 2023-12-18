
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path is None or suffix is None:
        return []
    
    if len(path) == 0 or not os.path.exists(path):
        return []
    
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []
    
    if os.path.isdir(path):
        
        dir_content = os.listdir(path)
        
        files = []
        
        for dir_element in dir_content:
            
            element_path = os.path.join(path, dir_element)
                   
            element_files = find_files(suffix, element_path)

            files.extend(element_files)
    
    return files


def test_recursion():
    result = [
        './tests/testdir/subdir3/subsubdir1/b.c', 
        './tests/testdir/t1.c', 
        './tests/testdir/subdir5/a.c', 
        './tests/testdir/subdir1/a.c'
    ]

    suffix = ".c"
    path = "./tests/testdir"

    assert result == find_files(suffix, path)


def test_null():
    suffix = ".c"
    path = None

    assert [] == find_files(suffix, path)


def test_path():
    suffix = ".c"
    path = "./tests/testdir1"

    assert [] == find_files(suffix, path)


if __name__ == "__main__":
    test_recursion()
    test_null()
    test_path()
