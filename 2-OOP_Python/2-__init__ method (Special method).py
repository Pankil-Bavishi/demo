# __init__(self): It is a "Special Method" in Python.   (Must Include Double underscore)
#Here 'self' is automatically assigning it to the __init__ Method.
#Normally we used init to 'Initialize' the Variable, that's what the name it self suggests.
#we can Imagine as 'consructor'.
#The Idea behind that it will be getting called automatically. Where as in normally we are supposed to Call particular,
#   method name for calling it.

# __init__ will be calling for every Object at One Time, Let's say If we have 2 Onjects, Then it will gonna call 2 Times, for each Object.


class computer:

    def __init__(self,cpu,ram):     #'i5' goes to CPU as an Argument,
        self.cp = cpu                #Then it'll be assigned to the 'Object' which is 'self'.
        self.re = ram

    def config(self):
        print("Config is: ", self.cp,self.re)   #Here CPU, RAM not an Local Variable, CPU belong to an 'Object'. &
                                                # For referring an onject, we'll use like 'self.c = cpu'
# we are passing 'self' so that we can use it to Fetch the values.


com1 = computer('i5',16)    #we see passing 2 parameter, but Actually it has '3 parameter' 1: Object it self, 2: CPU, 3: RAM.
com2 = computer('Ryzen 3',8)

com1.config()
com2.config()