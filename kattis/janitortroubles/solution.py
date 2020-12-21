import math

# Bretschneider's formula, lifted from https://keisan.casio.com/exec/system/1322718508
d = list(map(int, input().split()))
s = sum(d)/2
print(math.sqrt((s-d[0])*(s-d[1])*(s-d[2])*(s-d[3]) - d[0]*d[1]*d[2]*d[3]*(math.cos(math.pi/2)**2)))
