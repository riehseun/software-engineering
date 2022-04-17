def openfile(file_path):
    """
    Reads in a file and store the content into an array.
    
    Args:
        file_path -- path to the file.
    
    Returns:
        A list of strings.
    """
    
    with open(file_path, 'r') as line:
        array = line.read().split("\n")
    return array


def convert_string_to_integer_in_list(array):
    """
    Converts the contents of array from type string to type integer.
    
    Args:
        array -- A list of strings.
    
    Returns:
        A list of integers.
    """
    
    return list(map(int, array))