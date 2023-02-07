#3inanarray

 #def has_33(nums):
     ##   pass

    ##has_33([1, 3, 3]) → True
    ##has_33([1, 3, 1, 3]) → False
   #has_33([3, 1, 3]) → False

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3:
            if nums[i+1] == 3:
                return True
            else: pass
        else: pass
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))