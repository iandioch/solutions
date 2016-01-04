intSqrt :: Integer -> Integer
intSqrt a = floor (sqrt (fromIntegral a))

getPairs :: Integer -> [(Integer, Integer)]
getPairs 1 = map (\x -> (1, x)) [1..999]
getPairs n = (getPairs (n-1)) ++ (map (\x -> (n, x)) [1..n])

square :: Integer -> Integer
square x = x*x

getC :: Integer -> Integer -> Integer
getC a b = 1000 - a - b

isValidTrio :: Integer -> Integer -> Integer -> Bool
isValidTrio a b c = (((square a) + (square b)) == (square c)) && ((a + b + c) == 1000)

isValid :: (Integer, Integer) -> Bool
isValid p = isValidTrio (fst p) (snd p) (getC (fst p) (snd p))

correctPair :: (Integer, Integer)
correctPair = (head (filter (isValid) (getPairs 1000)))

ans :: Integer
ans = (fst correctPair)*(snd correctPair)*(getC (fst correctPair) (snd correctPair))

main = print ans