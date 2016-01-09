threes :: Int -> String
threes 1 = "1\n"
threes n = (show n) ++ (if n `mod` 3 == 0 then (" 0\n" ++ threes(n `div` 3)) else (if n `mod` 3 == 1 then (" -1\n" ++ threes((n-1) `div` 3)) else (" +1\n" ++ (threes((n+1) `div` 3)))))

main = putStr $ threes 31337357