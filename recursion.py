def fun(x,n):
    if(n==0):
        return
    print(x)
    fun(x,n-1)
fun(15,4)



def fun(i,n):
    if(i>=n):
        return
    print(i)
    fun(i+1,n)
fun(1,4)