# Assume it's a Secret and Private Code, Which was Hidden from the Developer for the Security Purpose.
def div(a,b):
    print(a/b)

# Whenever we don't have access to use the Any of the Functions that time it'll be Most Useful.
# It may restricted for the further use and don't have access to systems any Files, Key data, etc..
# It'll change the Functions inner mechanisms(Logics) based on what we have want.
#


# Function inside a Function (Pass Function as a Parameter)
# because everything in python is 'Object'.
#

def smart_div(func):

    # It's a Logic which is Similar to the Main Logic, but just replaced with our own Logic.
    def inner(a,b):
        if a<b:
            a,b = b,a # Swapping value of Numerator & Denominaor.
        return func(a,b)
    return inner


# NewFunc = FuncName(Original Func)
# div = smart_div(div)

# new_div = smart_div(div)
# new_div(2,4)
# Passing Function to Another Function ! (It's Possible in Python, That's the Beauty of Python)
div = smart_div(div)
div(2,4)