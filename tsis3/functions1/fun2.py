#celciustofahr

def celtofahr(fahr):
    cel = (5/9)*(fahr - 32)
    return cel

fahr = int(input())
print(celtofahr(fahr))