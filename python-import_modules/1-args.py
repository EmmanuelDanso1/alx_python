#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]
    num_of_args = len(argv)
    
    if num_of_args == 0:
        print("0 arguments.")
    elif num_of_args == 1:
        print("1 argument:")
    else:
        print(f"{num_of_args} arguments:")

    if num_of_args == 0:
        print(".")
    else:
        for i, arg in enumerate(argv, 1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
