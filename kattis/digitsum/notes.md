Requires some number theory.

For every batch of 10 numbers, they will be identical except for the final number. That means you can just do `10*answer(nums//10)` to get the total of these in one tenth of the time. You then add `45` to this number, for each of the numbers you ignored.

If the number you are given does not evenly fall into a batch, then keep decrementing it and doing the digitsums of the numbers you meet, until you reach a number evenly divisible by 10.

Runs in 0.02s.
