#!/usr/bin/python3
# add_0.py
if __name__ == "__main__":
    a = 1
    b = 2
    from add_0 import add

    result = add(a, b)
    print("{a} + {b} = {result}".format(a=a, b=b, result=result))

