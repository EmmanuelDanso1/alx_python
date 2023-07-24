#!/usr/bin/python3
"""
Assigning a variable 2-variable_load.py and printing the value out
#2-variable_load.py
"""
a =  int()


def import_variable_load(file):
    with open(file) as v:
        new_code = compile(v.read(), file, 'exec')
        namespace = {}
        exec(new_code, namespace)
        return namespace.get('a', None)
"""
In order to make it not run, we use if statement if __name__ == __main__
"""
if __name__ == "__main__":
    imported_a = import_variable_load('2-variable_load.py')
    if imported_a is not None:
        print("The value of 'a is:", imported_a)
    else:
        print("The variable 'a' was not found in the file.")
