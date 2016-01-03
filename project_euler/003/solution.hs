factors :: Int -> [Int]
--factors n :: Integer -> Integer[]
factors n = (filter
	(\x -> n `mod` x == 0)
	[2,3..((floor $ sqrt $ fromIntegral n)+1)])	

isPrime n = (length $ factors n) == 0

main = print $ last  $ filter isPrime (factors 600851475143)
