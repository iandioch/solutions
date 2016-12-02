# The chance of a bit being zero in a random 32bit
# int is 1/2. The chance of it being zero after an
# OR with another random int is (1/2)*(1/2), which
# equals 1/(2**2). After ORing with n integers, it
# is 1/(2**n).

# The chance of having any certain bit be 1 in the
# result after one OR is 1 - 1/(2**2), and after n
# numbers are ORed together is (1 - 1/(2**n)). The
# chance that every bit is 1 is therefore
# (1 - 1/(2**n))**32. This is a cumulative
# distribution function (cdf). 

# cdf(i) - cdf(i-1) gives the probability that the
# result is all 1's is between (i-1) and (i) ORs.
# We can sum these for each i from 1 to inifinity,
# until until the result is so small it is
# irrelevant in our desired precision.

from decimal import *
getcontext().prec = 15

def cdf(x):
	if x == 0:
		return Decimal(0)
	return (Decimal(1) - Decimal(1)/(Decimal(2)**x))**32


ans = Decimal(0)
i = 1
while True:
	y = cdf(i) - cdf(i-1)
	if y < Decimal('0.' + ('0'*14) + '1'):
		break
	ans += Decimal(i)*y
	i += 1

# messy way to get 10 digits after the decimal point
parts = str(ans).split('.')
print '%s.%s' % (parts[0], parts[1][:10])
