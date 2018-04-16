Use the sieve of Eratosthenes to get all of the primes. Then initialise one pointer to the first prime, and the second pointer to the highest prime below the target number. Then iterate, with the following logic:

- If the sum of these primes is too large, decrement the pointer to the higher prime.
- If the sum of these primes is too small, incremenet the pointer to the lower prime.
- If the sum is equal, add these primes to the answer set, and incrememnt the lower pointer.

This runs in 0.1s in python3.
