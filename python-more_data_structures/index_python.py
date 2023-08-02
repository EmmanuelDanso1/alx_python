#class Person:
#    pass
#p = Person()
#print(p)
"""
def who_am_i(income, own_business,investments):
    if income > 50000 or own_business:
        return "Entrepreneur"
    elif investments and not own_business:
        return "Investor"
    else:
        return "Employee"
print(who_am_i(40000, False, True))
my_tuple = (1,2,3,4,5)
result = my_tuple[1:4:2]
print(result)
"""
class User:
    id= 89
    name = "no name"
    _password: None
    def __init__(self,new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
u = User("John")
u.name
