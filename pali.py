def fun(s,left,right):
    if(left>=right):
        return True
    if(s[left]!=s[right]):
        return False
    return fun(s,left+1,right-1)
a='HELLo'
n=len(a)
result=fun(a,0,n-1)
print("String is",result)