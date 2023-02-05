a = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, 1]

is_float = lambda x : isinstance(x, float)
is_str = lambda x : isinstance(x, str)
def count_if(a, predicate):
    cnt = 0
    for i in a:
        if predicate(i):
            cnt +=1
        return cnt

print(count_if(a, is_float))
print(count_if(a, is_str))