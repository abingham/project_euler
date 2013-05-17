import Data.Char

_prod5 last_prod _ [] = []
_prod5 last_prod (0:a:b:c:d:e:hs) (t:ts) = (last_prod:_prod5 (a*b*c*d*e) (a:b:c:d:e:hs) ts)
_prod5 last_prod (h:hs) (t:ts) = (last_prod:_prod5 (last_prod `div` h * t) hs ts)

prod5 (a:b:c:d:e:xs) = _prod5 (a * b * c * d * e) (a:b:c:d:e:xs) xs

main = do
  input <- readFile "euler_08.input"
  print $ maximum $ prod5 [digitToInt i | i <- input, isDigit i]
