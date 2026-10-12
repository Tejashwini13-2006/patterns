
#Extraction of digits from number
n=5873
num=n
while(num>0):
    last_digit=num%10
    print(last_digit)
    num=num//10
    print(num)

#counting digits in a number
n=124587
num=n
count=0
while(num>0):
    count=count+1
    num=num//10
print(count)