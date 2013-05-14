(:require [clojure.contrib.math :as math])

(defn is_prime [x]
  (cond (= 0 x) false
        (= 1 x) false
        (= 2 x) true
        (some #(zero? (mod x %)) (take-while (partial > (sqrt x)) primes)) false
        :else true))

(def primes
  (filter is_prime (range)))

(println (take 10) primes)
