; 2520 is the smallest number that can be divided by each of the
; numbers from 1 to 10 without any remainder.
;
; What is the smallest positive number that is evenly divisible by all
; of the numbers from 1 to 20?

(ns project-euler.problem5)

(def divisors (reverse [11 12 13 14 15 16 17 18 19 20]))

(defn run []
  (first 
   (filter
    (fn [x]
      (every? #(= 0 (mod x %)) divisors))
    (drop 1 (range)))))
 
