#Volume of the sphere
#v = 4/3pi*r^2
import math

rad = int(input())
def vol(rad):
    return (4 * 3.14 * (rad ** 0.5))/3

print(vol(rad))