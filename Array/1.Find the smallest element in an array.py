# addition of feature of finding the kth element 
#this logic can solve 1,2,3 of this sheet 
def smallest(nums,k):
    return sorted(nums,reverse=True)[k-1]


print(nums)

smallest([2,3,1,0],2)