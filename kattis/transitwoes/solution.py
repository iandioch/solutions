dep_time, arr_time, num_buses = map(int, input().split())
walk_dur = list(map(int, input().split()))
bus_dur = list(map(int, input().split()))
bus_period = list(map(int, input().split()))

curr = dep_time + walk_dur[0]
for i in range(num_buses):
    wait = bus_period[i] - (curr % bus_period[i]) # todo:check
    curr += wait
    curr += bus_dur[i]
curr += walk_dur[-1]
print('yes' if curr <= arr_time else 'no')
