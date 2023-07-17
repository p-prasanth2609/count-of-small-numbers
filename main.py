nums=list(map(int,input().split()))

l=[]
for i in range(len(nums)):
    count=0
    for j in range(i+1,len(nums)):
        if(nums[i]>nums[j]):
            count+=1
    l.append(count)
print(l)

