n=153
num=n
total=0
p=len(str(n))
while(num>0):
    ld=num%10
    total=total+(ld**p)
    num=num//10
if(n==total):
    print("given number is an armstrong")
else:
    print("not an armstrong number")
