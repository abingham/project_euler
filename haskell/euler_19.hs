-- Is a year a leap year?
leapYear :: Int -> Bool
leapYear y | y `mod` 400 == 0 = True  -- century divisible by 400
           | y `mod` 100 == 0 = False -- century not divisible by 400
           | y `mod` 4 == 0   = True  -- non-century divisible by 4
           | otherwise        = False -- non-century not divisible by 4

normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

-- Given a year, this generates a list of days-of-the month.
daysOfMonths :: Int -> [Int]
daysOfMonths year =
  let
    counts = if leapYear year then leap else normal
  in
    concat [[1..n] | n <- counts]
    
main = 
  let
    dow = cycle [2,3,4,5,6,7,1] -- Jan 1 1901 is a Tuesday.
    dom = concat [daysOfMonths y | y <- [1901..2000]]
    sundayFirsts = [x | x <- zip dow dom, (fst x) == 7, (snd x) == 1]
  in
   print $ length sundayFirsts
