-- This calculates a level in Pacal's triangle based on the last
-- level.
next_level :: [Integer] -> [Integer]
next_level l = [1] ++ [l !! n  + l !! (n + 1) | n <- [0..(length l) - 2]] ++ [1]
                                                       
-- List of the levels of Pascal's triangle
pascals_triangle = [1] : [next_level (pascals_triangle !! n) | n <- [0..]]

-- calculate the number of paths through a lattice with sides of a
-- given size.
num_paths :: Int -> Integer
num_paths size = 
  let
    level = pascals_triangle !! (size * 2)
    middle_idx = div (length level) 2
  in
   level !! middle_idx

main = do
  print $ num_paths 20