#unique elements

a = list(map(int, input().split())) #array input
u = [] #empty list

def unique(a, u):
    if a not in u:
        u.append(a)  #adding and checking if theres repeated values
    
for i in range(len(a)):
    unique(a[i], u)    #using unique func
    
print(u)