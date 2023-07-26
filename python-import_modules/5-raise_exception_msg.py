#!/usr/bin/python
#raising a name exception with a message
def raise_exception_msg(message=""):
    try:
        raise NameError("")
    except NameError as e:
        print("")
