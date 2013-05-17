import Data.List

collatz :: Int -> Int
collatz x | even x = div x 2
          | otherwise = (3 * x) + 1

collatz_length :: Int -> Int
collatz_length 1 = 1  
collatz_length n = 1 + (collatz_length $ collatz n)

-- TODO: In parallel? vector-based caching?
main = do
  print $ fst $ foldl1' max [(collatz_length n, n) | n <- [1..999999]]

-- This is a caching version, storing values in a map.
-- collatz_lengths :: Map Int Int -> Int -> Map Int Int
-- collatz_lengths cache n =
--   if member n cache then
--     cache
--   else
--     let 
--       cn = collatz n
--       ncache = collatz_lengths cache cn
--     in
--      insert n (1 + (ncache ! cn)) ncache
        
-- main = 
--   let
--     lengths = L.foldl' collatz_lengths (fromList [(1,1)]) [2..999999]
--   in
--    print $ L.maximumBy (\a b -> compare (snd a) (snd b)) (toList lengths)

