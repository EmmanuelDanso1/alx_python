"""
printing numbers in ascending orders
"""
for num in range(100):
    print("{:02d}".format(num), end="")
    if num != 99:
        print(", ", end="")
    else:
        print()


