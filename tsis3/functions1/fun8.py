#007number

#def spy_game(nums):
    #pass

    #spy_game([1,2,4,0,0,7,5]) --> True
    #spy_game([1,0,2,4,0,5,7]) --> True
    #spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    s = ''  #empty storage
    for i in range(len(nums)): #iterating btw the range
        if nums[i] == 0 or nums[i] == 7:
            s+=str(nums[i]) #adding 007 to storage
    if '007' in s: #checking if 007 is contained here
        return True
    else:
        return False
            

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))