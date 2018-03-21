s = input()
curr = ''
indent = 0

lines = []
for c in s:
    curr += c
    if curr == '{':
        lines.append('{}{}'.format(' '*indent, c))
        curr = ''
        indent += 2
    elif curr.endswith('}') or curr.endswith('},'):
        d = curr.find('}')
        if len(curr[:d]) > 0:
            lines.append('{}{}'.format(' '*indent, curr[:d]))
        indent -= 2
        lines.append('{}{}'.format(' '*indent, curr[d:]))
        curr = ''
    elif curr[-1] == ',':
        lines.append('{}{}'.format(' '*indent, curr))
        curr = ''

# remove commas trailing afer }s
for j in range(len(lines)-1, -1, -1):
    if lines[j].strip() == ',':
        del lines[j]
        lines[j-1] += ','

print('\n'.join(lines))
