#histogram

a = list(map(int, input().split()))

def histo(a):
    for i in a:
        for x in range(i):    #to iterate inside the array to put stars
            print('*', end='')
        print('')
        
histo(a)