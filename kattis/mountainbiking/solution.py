import math

num_seg, gravity = input().split()
num_seg = int(num_seg)
gravity = float(gravity)

d = []

for i in range(num_seg):
    dist, angle_deg = map(int, input().split())
    rad = math.radians(angle_deg)
    accel = gravity*math.cos(rad)
    d.append((dist, rad, accel))

for i in range(num_seg):
    vel = 0
    for dist, rad, accel in d[i:]:
        newvel2 = vel*vel + 2*accel*dist
        vel = math.sqrt(newvel2)
    print(vel)
