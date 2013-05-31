(ns project-euler.problem9
  (:require [project-euler.util :as util]))

(defn pythagorean-triplets [sum]
  (for [a (range 1 (- sum 2))
        b (range (+ a 1) (- (- sum 1) a))
        c [(- sum a b)]
        :when (= (+ (util/expt a 2) (util/expt b 2)) (util/expt c 2))]
    [a b c]))

(defn run []
  (reduce * (first (pythagorean-triplets 1000))))
  
  
