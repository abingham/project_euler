count = 100

main = do
  print $ sum [x | x <- [1..count]] ^ 2 - sum [x ^ 2 | x <- [1..count]]