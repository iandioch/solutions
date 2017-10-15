notes = 'A, A#, B, C, C#, D, D#, E, F, F#, G, G#'.split(', ')
steps = [2, 2, 1, 2, 2, 2, 1]
scales = {}
for start in range(len(notes)):
	scale = [notes[start]]
	i = start
	for step in steps:
		i = (i+step)%len(notes)
		scale.append(notes[i])
	scales[notes[start]] = set(scale)

input()
song = input().split()
ans = []
for note in notes:
	if all(c in scales[note] for c in song):
		ans.append(note)

if len(ans) == 0:
	print('none')
else:
	print(' '.join(ans))
