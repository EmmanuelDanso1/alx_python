#!/usr/bin/python3
#raising a type exception
def raise_exception():
    try:
        raise "TypeException"
    except Exception as e:
        print("Exception has been raised")
