def merge(left,right):
    result=[]
    i=0
    j=0
    n,m=len(left),len(right)
    while(i<n and j<m):
        if(left[i]<=right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        while(i<n):
            result.append(left[i])
            i+=1
        while(j<m):
            result.append(right[j])
            j+=1
        return(result)
def mergesort(arr):
    if(len(arr)<=1):
        return(arr)
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left=mergesort(left_arr)
    right=mergesort(right_arr)
    return merge(left,right)
nums=[1,2,4,5,8,6,3,9,10,23,54]
print(mergesort(nums))

        
