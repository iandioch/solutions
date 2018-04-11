A number theory problem.

The sum of numbers in the range [start, start+v-1] is given by `(start+v-1)(start+v)//2 - (start-1)(start)//2`, which breaks down to `v*(2*start + v - 1)//2`

ie. Given `n`, we want to find a solution for `start` and `v` for: `n = v*(2*start + v - 1)//2`. This can be reformulated as `start = ((2*n)//v - v + 1)//2`.

The first equation above means that `v` must be a factor of `2*n`. What's more, for the integer division to work out, `(2*n)//v - v + 1` must be divisible by 2, which means `((2*n)//v - v) % 2 == 1`.

We can now just iterate `v` up to `sqrt(n*2)`, and find a solution. This runs in 0.75s.

However, [there are no valid solutions for `n = 2**k`](https://math.stackexchange.com/questions/94491/a-proof-that-powers-of-two-cannot-be-expressed-as-the-sum-of-multiple-consecutiv). Discarding powers of two (ie. the worst case) earlier brings the runtime to 0.04s.
