#!/usr/bin/python3
def best_score(a_dictionary):
    maximum_value = None
    maximum_key = None


    for key, value in a_dictionary.items():
        if maximum_value is None or value > maximum_value:
            maximum_value = value
            maximum_key = key
    return maximum_key
