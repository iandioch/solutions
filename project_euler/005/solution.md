This problem can be solved on paper.

Start with the product = 1
Take an integer n = 2
Keep incrementing n up until 19, and for each step, multiply the product by (n/gcd(product, n))

n = 2, product = `1*2`
n = 3, product = `1*2*3`
n = 4, product = `1*2*3*2`
n = 5, product = `1*2*3*2*5`
n = 6, product = `1*2*3*2*5`
n = 7, product = `1*2*3*2*5*7`
n = 8, product = `1*2*3*2*5*7*2`
n = 9, product = `1*2*3*2*5*7*2*3`

The product is at this point `1*2*3*2*5*7*2*3`, which equals 2520, the example answer.

If we continue iterating up, we get a product of `1*2*3*2*5*7*2*3*11*13*2*17*19`, which equals 232792560

