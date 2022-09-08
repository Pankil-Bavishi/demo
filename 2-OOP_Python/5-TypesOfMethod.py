#Variable: To Store the Data
#Methods(Behaviour): For the Behaviour OR To Perform some 'Operation'

# There are '3 Types of Methods':
#1 - Instance Method: (i)  Accessor Method: Only Responsible to work with 'Instance Varible' OR (Fetch the Values of Instance Variable)
                    # (ii) Mutator Method: If you want to Modify the Values, we'll use 'Mutator'.
#2 - Class Method: It's work wih Class Variable.
#3 - Static Method: If we Want any Method, which has nothing to do with Instance Variable & Class Variable, but we want Something Extra or,
     # which is not Concern with Variables, At that you will be using 'Static Method'.

#NOTE: 'Class & Static Variable' are 'SAME' in Variable, Where as 'Class & Static Method' are 'DIFFERENT' in Method.

class Student:

    school = 'Oxford'               #Class Variable - can be used with Class Method

    def __init__(self,m1,m2,m3):    #Instace Variable - can be used with Instance Method
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):      #Instace Method(because we are passing 'self' and it means its belongs to Particular Object | its works with Object.)
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchool(cls):     #Print the School Name | If we working with Instance Values - 'self' keyword & Working with Class Variable - 'cls' keyword.
        return cls.school

    @staticmethod
    def info():     #Static Method (No Class, No Object/Instance Variable)
        print("This is Student class.. in abc Module")

#    def get_m1(self):          # Getter/Fetch the Values/ Access
#        return self.m1

#   def set_m1(self,value):     #We can Use Constructor to Pass the Value or you can Set does. # Setter/Change the Value/Mutator.
#        self.m1 = value


s1 = Student(34,47,32)
s2 = Student(89,32,12)


# print(s1.m1)    #1'st Ways OR we can create the Method for 'M1' for Fetching its Marks.

print(s1.avg())
print(s2.avg())

print(Student.getSchool())
Student.info()












