import os


def find_files(suffix: str, path: str) -> list[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    if not os.path.isdir(path):
        return []
    return_list = find_files_rec(suffix, path)
    return_list.sort()
    return return_list


def find_files_rec(suffix: str, path: str) -> list[str]:
    """
    Recursively find files with a given suffix in the specified directory.

    Parameters:
    -----------
    suffix : str
        The suffix to search for in file names.
    path : str
        The directory path to search in.

    Returns:
    --------
    List[str]
        A list of paths to files that match the given suffix.
    """
    result = []  # Initialize an empty list to store found files
    dirs = os.listdir(path)

    for item in dirs:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            # Recursively find files in the subdirectory
            result.extend(find_files_rec(suffix, item_path))
        elif os.path.isfile(item_path) and item_path.endswith(suffix):
            result.append(item_path)

    return result  # Return the combined results


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    print(result)
    assert result == [
        "./testdir/subdir1/a.c",
        "./testdir/subdir3/subsubdir1/b.c",
        "./testdir/subdir5/a.c",
        "./testdir/t1.c",
    ]

    # Test Case 2: Not existing termination in the test folder
    print("Test Case 2: Not existing file termination")
    result = find_files(".py", "./testdir")
    print(result)
    assert result == []

    # Test Case 3
    print("Test Case 3: Non existing header files file termination")
    result = find_files(".hpp", "./testdir_faulty_name")
    print(result)
    assert result == []
