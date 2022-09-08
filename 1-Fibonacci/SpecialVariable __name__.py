# First Module Name is always '__Main__' It's the Point of Execution that's Where your code Starts.
# Let's say : Calc

#print("Hello : " + __name__)
# But, If you 'import calc' in other files : It'll print 'calc content' + 'Name of Modules(Here, calc)' on Particular File.'




# Let's say Demo :

#import calc
#print("Demo says : " + __name__)

#It'll print : Hello calc
# Then, Demo says : __main__

# If you print __name__ in calc : It'll Print only '__main__'


#2'nd Example :

# File : calc

# import demo   #even if imported as Demo,its shows only 'calc content' not 'demo content' because Demo content Run only,
#       when its a First program. Here in this case ita 2'nd file.

# print("It's Time to Go to Picnic")




# File : demo

# def main():
#     print("Hello")
#     print("Welcome User")
#
# if __name__ == "__main__":
#     main()


#Its Run Demp is a First Program to be Run.