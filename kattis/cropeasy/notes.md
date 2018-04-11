We do not care about individual points. We only care about those point coordinates mod 3. This is because a valid triangle is one where the sums of X coordinates and the sums of Y coordinates are both equal to zero mod 3.

Thus, we only keep track of the counts of coordinates with given coordinate values mod 3.

For each loop from 0 to 9, we map each of these values to an X and Y mod 3.

In the outermost loop, we check if we can combine 3 points with the same mod values in their coordinates. If N points have these exact coordinate mod values, then there are (N) * (N-1) * (N-2) combinations of these points. Divide this number by 6 (ie. 3 factorial) to get the number of unique combinations of these points.

Then in the next loop, we check if we can combine 2 points with the same mod values, and one other point. We check if we have enough points, and if the sums of their coordinates are equal to zero mod 3. We create a similar product as above, and divide by 2 (ie. 2!), as this is the number of ways of arranging them, to get the number of unique combinations.

Finally, in the innermost loop, we check if we can combine 3 points with unique coordinate values mod 3.

`cropeasy` runs in 0.2s in python3 with this method, and `crophard` in 0.22s.
