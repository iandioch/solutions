A number theory question.

From [this blog](https://www.johndcook.com/blog/2015/10/06/number-of-digits-in-n/), I got an understanding of Stirling's approximation, and how it can be used to estimate factorials. The number of digits in this estimate is the same as the number of digits of the real factorial for all N up to one million.

For some small N < 10, there are multiple factorials with the same number of digits, so I hardcoded those. For the rest, I iterated up to find the right N.

The [Kamenetsky formula](https://oeis.org/A034886) would probably suit better.
