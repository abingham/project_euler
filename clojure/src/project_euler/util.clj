(ns project-euler.util)

;; (def fibs
;;   ((fn rfib [a b] 
;;      (lazy-seq (cons a (rfib b (+ a b)))))
;;    1 2))

; Taken from clojure-contrib
(defn fibs
  "Returns a lazy sequence of all the Fibonacci numbers."
  []
  (map first (iterate (fn [[a b]] [b (+ a b)]) [0 1])))

; Taken from old clojure-contrib
(def primes
  (concat
   [2 3 5 7]
   (lazy-seq
    (let [primes-from
          (fn primes-from [n [f & r]]
            (if (some #(zero? (rem n %))
                      (take-while #(<= (* % %) n) primes))
              (recur (+ n f) r)
              (lazy-seq (cons n (primes-from (+ n f) r)))))
          wheel (cycle [2 4 2 4 6 2 6 4 2 4 6 6 2 6 4 2
                        6 4 6 8 4 2 4 2 4 8 6 4 6 2 4 6
                        2 6 6 4 2 4 6 2 6 4 2 4 2 10 2 10])]
      (primes-from 11 wheel)))))

;; (defn is_prime [x]
;;   (cond (= 0 x) false
;;         (= 1 x) false
;;         (= 2 x) true
;;         (some
;;          #(zero? (mod x %))
;;          (take-while
;;           (partial >= (Math/sqrt x))
;;           primes)) false
;;         :else true))

;(def primes
;  (filter is_prime (range)))

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

(defn digits [x]
  (if (< x 10) x
      (let [q (unchecked-divide-int x 10)
            r (mod x 10)]
        (lazy-seq (r (digits q))))))
