nums=[5,6,9,2,1,3,4,7,8]
n=len(nums)
for i in range (0,n):
    minindex=i
    for j in range(i+1,n):
        if(nums[j]<nums[minindex]):
            minindex=j
    temp=nums[i]
    nums[i]=nums[minindex]
    nums[minindex]=temp
print(nums)



