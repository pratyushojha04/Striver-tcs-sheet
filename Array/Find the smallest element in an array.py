# addition of feature of finding the kth element 
def smallest(nums,k):
    return sorted(nums,reverse=True)[k-1]


print(nums)

smallest([2,3,1,0],2)