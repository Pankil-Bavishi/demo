# Variable : 2 Types
# 1: Instance Variable: because as your 'Path' changes, as the 'Object' changes, This Value also Change.
# 2: Class(Static) Variable

# In your Memory, we have Different Namespace:
#       The Place where you can Create 'an Object or Variable', called as Namesapce.

# There are '2 Types' of Namespace:
# 1: Clas Namespace: Where you will Store all the Class Variable
# 2: Object/Instance Namespace: Where you will Create all the Instance Variable.

#Here we gonna take an example of 'CAR', and it also has feature like its Company Name, Mileage, Engine, etc..


class car:
    wheels = 4              # Outside __init__: is known as 'Class(Static) Variable' & its belongs to 'Class Namespace'.

    def __init__(self):     #Inside __init__: is known as 'Instace Variable' & its belongs to 'Instance Namespace'.
        self.mil = 10
        self.com = "BMW"

c1 = car()
c2 = car()

c1.mil = 22

car.wheels = 5  #The momnet we chnage the Values of 'Wheels', it'll affect the 'All Objects' right, because 'they are Shared'. Means,
                # This wheel is 'Shared between all the Objects'.

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)