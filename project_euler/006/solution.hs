square :: Integer -> Integer
square n = n*n

normalSum :: Integer -> Integer
normalSum n = foldl (+) 0 [0..n]

squareSum :: Integer -> Integer
squareSum n = foldl (+) 0 (map square [0..n])

main = print ((square $ normalSum 100) - (squareSum 100))