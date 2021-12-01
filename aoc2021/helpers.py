import inspect
import os.path

def input():
    path = inspect.stack()[1].filename 
    file = os.path.splitext(os.path.basename(path))[0]
    return open("inputs/" + file + ".txt", 'r').read()

