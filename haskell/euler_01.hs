import EulerUtil

multipleOf3 :: Int -> Bool
multipleOf3 x
    | (sum $ digits x) `mod` 3 == 0 = True
    | otherwise = False

multipleOf5 :: Int -> Bool
multipleOf5 x = 
    case last $ digits x of
      0 -> True
      5 -> True
      otherwise -> False

main = do
  print $ sum [x | x <- [1..999], multipleOf3 x || multipleOf5 x]