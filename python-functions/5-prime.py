def is_prime(number):
    if number < 2:
     return False
    for  i in range(2, int(number ** 0.5) +1):
     if number % 1 == 0:
        return False
    return True
"""
number = 7
new_number = is_prime(number)
print(new_number)
"""