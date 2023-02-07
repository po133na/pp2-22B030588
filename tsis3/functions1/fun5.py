#permutation
import itertools

def perms(str):
    if len(str) == 0:
        return ['']
        #generation of remaining perms in str
        remain = perms(str[1:len(str)])
        
        #generation by inserting 1st char
        permone = []
        for i in range(0, len(remain)):
            for j in range(0, len(str)):
                #new str <- first char
                nstr = remain[i][0: j] + str[0] + remain[i][j: len(str) - 1]
                if nstr not in permone:
                    permone.append(nstr)
                    return permone #returning results

inp = input()
print(perms(inp))