I initially thought of binary searching the curve to find the maximum. However, instead we can use calculus. Go maths!

Given `y = -aX^2 + bX + c` (`X = R`, `Y = T`, if you use the variable names from the question), `dy/dx = -2aX + b = 0`. We can go from here to `X = b/2a`. We now know we'll reach the max at this `X` value, so we can sub it in to the original equation. We can simply do this for all inputs and output the one with the maximum.
