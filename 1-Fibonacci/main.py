def fib(n):
    a=0
    b=1
    if n == 1 or n == 0:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c=a+b
            if c > 100:
                break
            a=b
            b=c
            print(c)

fb = int(input("Enter Fibonacci Number: "))

if fb < 0:
    print("Please Enter Value Greater than 0(Positive Number)")
else:
    fib(fb)