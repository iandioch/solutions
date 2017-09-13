d = {
    'thou': 1,
    'th': 1,
}
d['inch'] = d['th']*1000
d['in'] = d['inch']

d['foot'] = d['in']*12
d['ft'] = d['foot']

d['yard'] = d['ft']*3
d['yd'] = d['yard']

d['chain'] = d['yd']*22
d['ch'] = d['chain']

d['furlong'] = d['ch']*10
d['fur'] = d['furlong']

d['mile'] = d['fur']*8
d['mi'] = d['mile']

d['league'] = d['mi']*3
d['lea'] = d['league']

quant, unit, _, desired = input().split()
quant = float(quant)

thou = quant*d[unit]
ans = thou/d[desired]
print(ans)
