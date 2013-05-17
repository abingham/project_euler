import Data.Maybe
import List

max_div = 20

main = do
  print $ fromJust $ find (\x -> and [x `mod` den == 0 | den <- [max_div,max_div-1..2]]) [max_div..]