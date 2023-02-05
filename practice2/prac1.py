#minmaxsum

def miniMaxSum(a):
    a.sort()
    min, max = sum(a[:-1]), sum(a[1:])

    return min, max

minSum, maxSum = miniMaxSum([1, 3, 5, 7, 9])

print(f"Min sum is {minSum}\nMax sum is {maxSum}")