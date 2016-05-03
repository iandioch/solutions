import sys

limit = 200

d = [sys.maxint for i in xrange(limit+1)]

"""
Very proud to have gotten this much on my own;
It doesn't seem that far away from how the first solvers did it.

Using star sequences (TIL!) to calculate addition chains.
I knew that was what I was going for fairly quickly,
But I didn't know what they were called.

It's OEIS sequence A003313, and it's cool maths.

The star sequence method fails to give the right answer for some
bigger numbers, but it is a-okay for n <= 200.
"""
def step(chain):
    n = chain[-1] 
    if len(chain)-1 <= d[n]:
        d[n] = len(chain)-1
    else:
        return
    for i in chain:
        m = n + i

        if m > limit:
            continue
        c = chain[:]
        c.append(m)
        step(c)


step([1])

print sum([d[i] for i in xrange(1, 201)])
