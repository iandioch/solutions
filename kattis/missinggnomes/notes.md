We don't need to get any permutations - we just need to distribute the remaining numbers in the correct places in the given list to produce the lexicographically smallest result.

1. Get the list of input numbers, `A`.
2. Get a sorted list of the numbers you still need to add to the set, `B`.
3. Create 2 pointers, initialising them to the start of each list, `i` and `j`.
4. While `i < len(A)` and `j < len(B)`, if `A[i] < B[j]`, output `A[i]` and increment `i`; otherwise, output `B[j]` and increment `j`.
5. Output all remaining numbers (only one of `A` and `B` will still have remaining numbers, and they will already be in the required order).
