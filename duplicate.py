nums=[1,2,3,3]

seen=set()
for num in nums:
    if num in seen:
     print(True)
     break
    else:
     seen.add(num)
else:
    print(False)
    