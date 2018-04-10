Instead of keeping lists of numbers that are inputted, keep counts of how many of each number have been inputted (as there are guarantees to have 100 copies of each inputted number in the worst case).

Then starting at the highest A and lowest B (as the lowest max sum will always pair the highest from one set with the lowest from the other), see if that sum is greater than the max. Then throw away all copies of the used numbers that you can, and move onto the next highest A and lowest B with copies remaining.

You cannot just take the overall max(A) and min(B), and min(A) and max(B), as it would fail the following test case:

```
3
1 9
6 6
9 1
```

Expected output:

```
10
12
12
```

Output from this procedure:

```
10
12
10
```
