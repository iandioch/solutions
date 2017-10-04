import sys
for line in sys.stdin.readlines():
    *state, eggs, surv_larv, surv_pup, num_weeks = map(int, line.split())
    for week in range(num_weeks):
        num_mosq, num_pup, num_larv = state
        
        new_pup = num_larv // surv_larv
        new_mosq = num_pup // surv_pup
        new_larv = num_mosq * eggs
    
        state = (new_mosq, new_pup, new_larv)
    print(state[0])
