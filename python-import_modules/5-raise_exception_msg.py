#!/usr/bin/python
#raising a name exception with a message
def raise_exception_msg(message=""):
    try:
        raise ("")
    except Exception as e:
        print("{} ",e)
    