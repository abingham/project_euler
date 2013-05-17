fib :: Int -> Int
fib n = fibs!!n

fibs :: [Int]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

main = print $ sum [x | x <- takeWhile (\x -> x <= 4000000) fibs, even x]