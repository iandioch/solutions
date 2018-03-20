words = input().split()
t = len(words)
f = len([w for w in words if 'ae' in w])
if f*10/t >= 4:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')
