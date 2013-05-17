pythagorean_triplets sum = [[a,b,1000 - a - b] | a <- [1..(sum - 2)], b <- [a..((sum - 1) - a)], a^2 + b^2 == (sum - a - b) ^ 2]

main = (print.product.head) $ pythagorean_triplets 1000