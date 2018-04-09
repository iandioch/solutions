We only care about whether any number in the sequence is above or below the given desired median (`B`).

Thus, we build a new sequence `r`, where:

```
if A[i] == B:
    r[i] = 0
elif A[i] > B:
    r[i] = 1
else:
    r[i] = -1
```

We then start at the position of `B` in this array, and step rightwards, keeping a running sum of `r[i]` for each `i`. We keep a tally `cnt` of how many times we have seen each sum.

We then step leftwards from `B`, again keeping a running sum. If at any step our running sum is `c`, then we know we have found `cnt[-c]` new subsequences that will have median `B`.
