from functools import reduce

#For Doubles:
# def update(n):
#     return n*2

#For Reduce:
# def add_all(a,b):
#     return a+b

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n*2,evens))

sum = reduce(lambda a,b : a+b ,doubles)

print("Filter (EVEN)",evens)
print("Map (Double)",doubles)
print("Reduce (Sum All Value)",sum)