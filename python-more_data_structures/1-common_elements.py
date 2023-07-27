#!/usr/bin/python3
#returning common set
def common_elements(set_1, set_2):
    #common_set_returning = set_1 & set_2
    #return common_set_returning
    common_set_callback = set()

    for element in set_1:
        if element in set_2:
            common_set_callback.add(element)
    return common_set_callback
