isPalindrome :: [Char] -> Bool
isPalindrome s = (length s <= 1) || (((head s) == (last s)) && (isPalindrome (tail (init s))))

getPalindromeProducts :: Int -> [Int]
getPalindromeProducts n = filter (\n -> isPalindrome $ show n) (map (\x -> x*n) [n..999])

maxNum :: [Int] -> Int
maxNum [] = 0
maxNum a = (maximum a)

getMaxPalindromeProduct :: Int -> Int
getMaxPalindromeProduct n = maxNum (getPalindromeProducts n)

maxPal :: Int
maxPal = maxNum (map getMaxPalindromeProduct [100..999])