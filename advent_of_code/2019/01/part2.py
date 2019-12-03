import sys

ans = 0
for line in sys.stdin.readlines():
    mass = int(line)
    fuel_req = mass//3 - 2
    while fuel_req > 0:
        ans += fuel_req
        fuel_req = fuel_req//3 - 2

print(ans)
