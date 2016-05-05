from math import factorial

# Standard n choose r function. Based off of Mark Tolonen's nCr here:
# http://stackoverflow.com/a/4941846/3536521
def nCr(n, r):
    return (0.0 + factorial(n))/factorial(r)/factorial(n-r)

# The answer is 7 * the probability that any one colour is present.
# The probability that a colour is present is 1 - nCr(60,20)/nCr(70,20),
# as the probability that a colour is present =
# (1 - the probability that the colour is absent)
# The probability that a colour is absent = nCr(60,20)/nCr(70,20)
# That is, the number of ways of choosing while avoiding the colour
# Divided by all of the ways of choosing

print 7*(1-(nCr(60, 20)/nCr(70, 20)))

