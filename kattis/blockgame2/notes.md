Given `a, b, a < b`.

There are three scenarios:

1. `b % a == 0`, in which case the current player wins.
2. `2*a < b`, in which case the current player can always win (as they can force their opponent into scenario 3, by leaving them with either `b % a, a`, or `a, b%a + a`, one of which is guaranteed to end in loss for the opponent).
3. `a < b < 2*a`, in which case there is only one possible move: `b-a, a`. The game simulation can then be continued.
