#!/usr/bin/python3
#removing lowercase 'c' and 'C' from alphabet
def no_c(my_string):
    result = ""
    for char in my_string:
        if char.lower() != 'c':
            result = result + char
    return result
#print(no_c("Holberton School"))
#print(no_c("Chicago"))
#print(no_c("C is fun!"))        