This is a dynamic programming problem. If there is an opening bracket at position `L`, we try each position `R` from this point in the string onwards to act as a closing bracket to match `L`. The number of possible subsequences after this forms is the number of sequences between this `L` and `R`, multiplied by the number of sequences between `R` and the end of the string.

We can optimise this by realising that all valid sequences have an even length, so we can iterate two steps at a time when finding our `R`. With some memoisation, this runs in 0.45s in Python3.

I had issues with the modular output of the answer, as the judge does not accept any zero-padded answers that should not be zero-padded. Ie. If the answer is `3`, then `00003` will not be accepted. However, if the answer is `200003`, then `00003` is what is expected. This was surprisingly annoying to get correct.`
