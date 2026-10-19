def factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        result=num*factorial(num-1)
        return (result)
w=int(input("enter a number"))
a=factorial(w)
print("factorial of a number is:",a)
