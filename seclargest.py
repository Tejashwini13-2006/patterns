arr=[10,25,99,85,96,98,100]
largest=float("-inf")
second=float("-inf")
for i in arr:
    if(i>largest):
        second=largest
        largest=i
    elif(i>second and i!=largest):
        second=i
print("second largest:",second)
