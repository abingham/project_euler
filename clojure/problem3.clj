(defn is_prime [x]
  (cond (= 0 x) false
        (= 1 x) false
        (= 2 x) true
        (some 
         #(zero? (mod x %))  
         (take-while (partial >= (Math/sqrt x)) 
                     (rest (rest (range))))) false
        :else true))

(def primes
  (filter is_prime (range)))

(defn prime_factors 
  ([x] (prime_factors x primes))
  ([x cands]
     (cond (= x 1) '()
           (zero? (mod x (first cands))) (cons (first cands) (prime_factors (/ x (first cands))))
           :else (prime_factors x (rest cands)))))

(println (last (prime_factors 600851475143)))

