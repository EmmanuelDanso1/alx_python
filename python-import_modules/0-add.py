# add_0.py
def add(a, b):
    return a + b
def import_add_function(file_name):
    with open(file_name) as f:
        code = compile(f.read(), file_name, 'exec')
        namespace = {}
        exec(code, namespace)
        return namespace.get('add', None)


if __name__ == "__main__":
    a = 1
    b = 2

    add_function = import_add_function('add_0.py')
    if add_function is not None:
        result = add_function(a, b)
        print("{} + {} = {}".format(a, b, result))
