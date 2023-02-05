#chickyrabbit

def solve(numheads, numlegs):
    chicks = (numlegs - numheads * 2) / 2
    rbts = numheads - chicks
    if chicks < 0 or rbts < 0 or int(chicks) != chicks or int(rbts) != rbts:
        return 0
    return int(chicks), int(rbts)

numheads = int(input())
numlegs = int(input())
ans = solve(numheads, numlegs)
if ans == 0:
  print("you are poor")
else:
  print("rbts:", ans[1])
  print("chicks:", ans[0])
