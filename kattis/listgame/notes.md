Th problem is simply asking for the count of prime factors of the given number.

The worst case input is 999999937. You need to iterate up from 2..n to find numbers that divide evenly. You can quit when your number >= sqrt(n), and it is necessary to do this to fit in the time limit.
