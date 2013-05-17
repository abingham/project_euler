import EulerUtil

-- Generate triangle numbers
triangles :: [Int]
triangles = scanl (+) 1 [2..]

main = do
  print $ head $ dropWhile ((< 501).num_divisors) triangles
  