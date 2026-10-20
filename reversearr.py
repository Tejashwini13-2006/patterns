def fun(arr,left,right):
    if(left>=right):
        return
    else:
        arr[left],arr[right]=arr[right],arr[left]
        fun(arr,left+1,right-1)
        print(arr)
num=[5,7,3,2,6,1,5,9]
fun(num,0,7)