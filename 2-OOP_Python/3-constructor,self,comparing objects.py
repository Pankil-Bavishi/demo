# Object : Every object holds its own size
#          Size of an object Depends on the no. of Variable & Size of each variable.

# Who allocates Size to Object ? (Who is Responsible for assigning / for calculating the memory ?) : 'Constructor'


# self: self is Pointing to or directing to Object based on what we are calling
# If we calling like: c1.update() then in the bracket its passing 'c1', then 'self' will be assigned to 'c1' and that's Important.
# because it is 'Referring' to an Object.
# If we have 10 Objects and refer to any 1, then we say 'self', it means 'Current Instance' you can say.

# Comparing Object: We can compare 2 Object by making our own functions (Here compare), which Takes 2 Parameters,
#   like: compare(who ic Calling,Whom to compare)
#Ex:      compare(self,c2) is because,  (Its a Function)
#         c1.compare(c2)        (Its How to call)

class computer:
    def __init__(self):
        self.name = 'Tata'
        self.age = 11

    def compare(self,c2):
        if self.age == c2.age:
            return True
        else:
            return False

c1 = computer()
c1.age = 15
c2 = computer()


if c1.compare(c2):      #Here 'compare' Function is User Defined Functions, not Built-in Function.
    print("They are Same")
else:
    print("They are Different")


print("C1 Name: ",c1.name)
print("C1 Name: ",c2.name)
print("--------------------")
print("C1 Age: ",c1.age)
print("C1 Age: ",c2.age)