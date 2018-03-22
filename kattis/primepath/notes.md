Compute all 4-digit primes before anything else, as they will be needed for many test cases. Can also pre-build a graph of what primes are 1 digit away from what other primes.

It is then a matter of doign a BFS from the starting number to the target number, with the help of a priority queue. To speed it up, I kept track of what digit was last changed, and do not jump to another prime by changing that digit again straight away. That would lead to infinte loops bouncing between 2 primes.
