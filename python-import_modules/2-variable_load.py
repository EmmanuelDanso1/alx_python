#!/usr/bin/python3
"""
Assigning a variable 2-variable_load.py and printing the value out
#2-variable_load.py
"""
a = 89
a = -100


def import_variable_load(variable_load_2):
    with open(variable_load_2) as f:
        new_code = compile(f.read(), variable_load_2, 'exec')
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
