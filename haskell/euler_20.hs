import Data.List
import EulerUtil

main = do
  print $ foldl1' (+) (digits $ factorial 100)