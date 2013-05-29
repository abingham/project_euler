(ns project-euler.util)

(def fibs
  ((fn rfib [a b] 
     (lazy-seq (cons a (rfib b (+ a b)))))
   1 2))

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

(defn palindrome? [x]
  (= x (clojure.string/reverse x)))

(defn expt [b p]
  (reduce * (repeat p b)))

(def sum (partial reduce +))
