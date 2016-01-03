-- memoized fibonacci
fib :: Int -> Int
fib x = if x < 1
		then 0
		else if x == 1 then 1
		else fibs!!(x-1)+fibs!!(x-2)
	where
	fibs = map fib[0..]

fibs n = [(fib x) | x <- [1..n]]

evenFibs n = [fib x | x <- [3,6..n]]

main = print (foldl (+) 0 (filter (\n -> n < 4000000) (evenFibs 34)))