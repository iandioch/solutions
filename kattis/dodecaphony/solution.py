notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
note_vals = {note:notes.index(note) for note in notes}

def get_transpositions(orig):
    for i in range(len(notes)):
        yield [notes[(note_vals[c] + i) % len(notes)] for c in orig]

def get_retrograde(orig):
    return orig[::-1]

def get_inversion(orig):
    base = note_vals[orig[0]]
    out = [orig[0]]
    for c in orig[1:]:
        diff = base - note_vals[c]
        note = notes[(base + diff) % len(notes)]
        out.append(note)
    return out

def main():
    melody_len = int(input())
    orig = input().split()
    mod = input().split()

    transpositions = get_transpositions(orig)
    if mod in transpositions:
        print('Transposition')
        return

    if mod == get_retrograde(orig):
        print('Retrograde')
        return

    if mod == get_inversion(orig):
        print('Inversion')
        return

    print('Nonsense')

main()
