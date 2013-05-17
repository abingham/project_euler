import EulerUtil

main = do
  print $ maximum $ filter (\x -> palindrome $ digits $ x) [x * y | x <- [100..999], y <- [100..999]]
