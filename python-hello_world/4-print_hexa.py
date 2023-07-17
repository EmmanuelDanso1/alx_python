#num = numbers_to_be_printed
#the output ranges from 0 to 98
"""
the :1d(decimal)  :1x(hexidecimal) ensures that theres only one decimal place
"""
for num in range(99):
    print('{:1d} = 0x{:1x}'.format(num,num))
