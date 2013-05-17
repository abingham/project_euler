-- Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
-- If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

-- For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

-- Evaluate the sum of all the amicable numbers under 10000.

import Data.List

proper_divisors :: Integral a => a -> [a]
proper_divisors x | odd x     = [y | y <- [1,3..div x 2], x `mod` y == 0]
                  | otherwise = [y | y <- [1..div x 2], x `mod` y == 0]

d :: Integral a => a -> a
d x = foldl' (+) 0 (proper_divisors x)

amicable :: Integral a => a -> Bool
amicable a 
  | a /= b = d(b) == a
  | otherwise = False
    where b = d(a)

main = do
  print $ foldl1' (+) [x | x <- [1..9999], amicable x]