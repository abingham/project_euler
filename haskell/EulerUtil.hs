module EulerUtil(digits, 
                 enumerate,
                 factorial,
                 num_divisors, 
                 palindrome, 
                 primes, 
                 prime_factors, 
                 run_lengths) where
import Char (digitToInt)
import Data.List (foldl')

factorial :: Integral a => a -> a
factorial x = foldl' (*) 1 [1..x]

enumerate :: [a] -> [(Int, a)]
enumerate x = zip [0..] x
--enumerate [] = []
--enumerate (x:xs) = 
--    do (0, x) : impl 1 xs
--    where
--      impl _ [] = []
--      impl idx (x:xs) = (idx, x) : impl (idx + 1) xs

digits :: Integral a => a -> [Int]
digits x = [digitToInt c | c <- show x]

-- source: http://www.haskell.org/haskellwiki/Prime_numbers
primes :: [Int]
primes = 2: 3: sieve [] (tail primes) 5
    where
      notDivsBy d n     = n `mod` d /= 0
      sieve ds (p:ps) x = foldr (filter . notDivsBy) [x, x+2..p*p-2] ds
                          ++ sieve (p:ds) ps (p*p+2)
                                         
_prime_factors :: Int -> [Int] -> [Int]
_prime_factors 1 _ = []
_prime_factors x (p:ps) =
    let (d,m) = divMod x p
    in pf' d m x (p:ps)
       where
         pf' d 0 _ (p:ps) = p : _prime_factors d (p:ps)
         pf' _ _ x (p:ps) = _prime_factors x ps
        
prime_factors :: Int -> [Int]
prime_factors x = _prime_factors x primes

-- Counts run-lengths in a sequence
run_lengths :: Eq a => [a] -> [(Int, a)]
run_lengths [] = []
run_lengths (x:xs) =
    let l = length (x:xs)
        new = dropWhile (== x) (x:xs)
    in ((l - (length new), x) : run_lengths new)

-- Counts the number of divisors of a number
num_divisors :: Int -> Int
num_divisors x =
    let c = run_lengths $ prime_factors x
    in foldl (*) 1 (map ((+ 1).fst) c)

palindrome :: Eq a => [a] -> Bool
palindrome [] = True
-- palindrome [x] = True
palindrome x = and [x!!i == x!!((length x) - i - 1) | i <- [0..length x `div` 2]]