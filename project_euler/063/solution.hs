lengthOfNum :: Integer -> Integer
lengthOfNum n = fromIntegral (length (show n))

isValidPair :: (Integer, Integer) -> Bool
isValidPair p = lengthOfNum ((fst p) ^ (snd p)) == (snd p)

getPairings :: Integer -> [(Integer, Integer)]
getPairings a = (map (\n -> (a, n)) [1..30])

countValidPairings :: [(Integer, Integer)] -> Int
countValidPairings a = length (filter isValidPair a)

main = print (foldl (+) 0 (map countValidPairings (map (getPairings) [1..9])))