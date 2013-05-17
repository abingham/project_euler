ones = ["", 
        "one", 
        "two", 
        "three", 
        "four", 
        "five", 
        "six", 
        "seven", 
        "eight", 
        "nine"]
       
teens = ["ten",
         "eleven",
         "twelve",
         "thirteen",
         "fourteen",
         "fifteen",
         "sixteen",
         "seventeen",
         "eighteen",
         "nineteen"]

tens = ["",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety"]

n2t :: Int -> Int -> Int -> [Char]
n2t h t o 
  -- If the number is round hundreds...
  | and [h > 0, t == 0, o == 0] = ones !! h ++ " hundred "
                                  
  -- If the number is > 100, but not roundly...
  | h > 0                       = ones !! h ++ " hundred and " ++ n2t 0 t o
                                  
  -- If the number is a "teen"...
  | t == 1                      = teens !! o
                                  
  -- If the number is a "-ty"...                                  
  | t /= 0                      = tens !! t ++ " " ++ n2t 0 0 o

  -- If the number is just ones...
  | o /= 0                      = ones !! o
  | otherwise                   = "zero"

number_to_text :: Int -> [Char]
number_to_text 1000 = "one thousand"
number_to_text x =
  let
    (valo, ones) = x `divMod` 10
    (valt, tens) = valo `divMod` 10
    (valh, hundreds) = valt `divMod` 10
  in
   n2t hundreds tens ones
   
main = do
  print $ length $ filter (\x -> x /= ' ') $ concat [number_to_text n | n <- [1..1000]]