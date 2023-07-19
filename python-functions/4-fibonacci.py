def fibonacci_sequence(n):
    sequence = []
    if n <= 0:
        return sequence
    elif n == 1:
        return [1]
    elif n == 2:
        return [0,1]
    else:
        sequence = [0,1]
#using range to iterate the function
        for i in range(2,n):
            next_iteration = sequence[i - 1]+ sequence[i - 2]
            sequence.append(next_iteration)
        return sequence
"""
n = 10
next_numbers = fibonacci_sequence(n)
print(next_numbers)
"""