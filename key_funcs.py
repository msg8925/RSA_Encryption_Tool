# Read a key from a file
from file_context_managers import Open_file

def read_from_file(filename, mode):
    
    with Open_file(filename, mode) as f:
        key = f.read()
        
    return key


